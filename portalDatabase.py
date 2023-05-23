import mysql.connector
from mysql.connector import Error


class Database():
    def __init__(self,
                 host="localhost",
                 port=3306,
                 database="banks_portal",
                 user='root',
                 password='IloveGhani1622'):

        self.host       = host
        self.port       = port
        self.database   = database
        self.user       = user
        self.password   = password
        self.connection = None
        self.cursor     = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host         = self.host,
                port         = self.port,
                database     = self.database,
                user         = self.user,
                password     = self.password)

            if self.connection.is_connected():
                return
        except Error as e:
            print("Error while connecting to MySQL", e)


    def getAllAccounts(self):
        if self.connection.is_connected():
            self.cursor= self.connection.cursor()
            query = "select * from accounts"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records

    def getAllTransactions(self):
        ''' Complete the method to execute
                query to get all transactions'''
        self.cursor= self.connection.cursor()
        query = "select * from transactions"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records

    def deposit(self, accountID, amount):
        ''' Complete the method that calls store procedure
                    and return the results'''
        self.cursor= self.connection.cursor()
        self.cursor.callproc('deposit', [accountID, amount,])
        self.connection.commit()
        return self.cursor.stored_results()


    def withdraw(self, accountID, amount):
        ''' Complete the method that calls store procedure
                    and return the results'''
        self.cursor= self.connection.cursor()
        self.cursor.callproc('withdraw', [accountID, amount,])
        self.connection.commit()
        return self.cursor.stored_results()


    def addAccount(self, ownerName, owner_ssn, balance, status):
        ''' Complete the method to insert an
                    account to the accounts table'''
        self.cursor= self.connection.cursor()
        query = "INSERT INTO accounts (ownerName, owner_ssn, balance, account_status) VALUES(%s,%s,%s,%s)"
        val = (ownerName, owner_ssn,balance, status,)
        self.cursor.execute(query,val)
        self.connection.commit()

    def accountTransactions(self, accountID):
        ''' Complete the method to call
                    procedure accountTransaction return results'''
        self.cursor= self.connection.cursor()
        self.cursor.callproc('accountTransactions', [accountID, ])
        data = []
        for result in self.cursor.stored_results():
            data=result.fetchall()
        print(data)
        return data

    def deleteAccount(self, AccountID):
        ''' Complete the method to delete account
                and all transactions related to account'''
        self.cursor= self.connection.cursor()
        query = "delete from transactions WHERE accountId = %s"
        val = (AccountID,)
        self.cursor.execute(query,val)
        query = "delete from accounts WHERE accountId = %s"
        val = (AccountID,)
        self.cursor.execute(query,val)
        self.connection.commit()




