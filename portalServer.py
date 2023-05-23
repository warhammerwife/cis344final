from http.server import HTTPServer, BaseHTTPRequestHandler
from os import curdir, sep
from portalDatabase import Database
import cgi

''' Class to handle get and post request of our HTTP server'''
class PortalRequestHandler(BaseHTTPRequestHandler):
    ''' Constructor to initalize database and HTTP request handler'''
    def __init__(self, *args):
        self.database = Database()
        BaseHTTPRequestHandler.__init__(self, *args)

    ''' Function to handle POST request which happen after click submit button of the form'''
    def do_POST(self):

        try:
            ''' Code to handle add account post request'''
            if self.path == '/addAccount': #This code handles the submission of form in Add Account
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                owner_name     = form.getvalue("oname")
                owner_ssn = int(form.getvalue("owner_ssn"))
                balance    = float(form.getvalue("balance"))
                acct_status = "active"
                ##Call the Database Method to a add a new student
                '''
                    Example call: self.database.addAccount(student_name, ownerName, owner_ssn, balance, status)
                '''
                self.database.addAccount(owner_name, owner_ssn,balance,acct_status) #It calls the addAccount function in portalDatabase
                print("grabbed values",owner_name,owner_ssn,balance)

                self.wfile.write(b"<html><head><title> Bank's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Bank's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addAccount'>Add Account</a>|\
                                  <a href='/withdraw'>Withdraw</a>|\
                                  <a href='/deposit'>Deposit </a>|\
                                  <a href='/searchTransactions'>Search Transactions</a>|\
                                  <a href='/allTransactions'>All Transactions</a>|\
                                  <a href='/deleteAccount'>Delete Account</a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Account has been added</h3>")
                self.wfile.write(b"<div><a href='/addAccount'>Add a New Account</a></div>")
                self.wfile.write(b"</center></body></html>")

            elif self.path == '/withdraw': # This code receives the POST request after we click on Submit in the withdrawal form
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                accountId = int(form.getvalue("accountId"))
                amount    = float(form.getvalue("amount"))

                self.database.withdraw(accountId,amount)# It calls the withdraw function in portalDatabase.py
                print("grabbed values",accountId, amount)

                self.wfile.write(b"<html><head><title> Bank's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Bank's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addAccount'>Add Account</a>|\
                                  <a href='/withdraw'>Withdraw</a>|\
                                  <a href='/deposit'>Deposit </a>|\
                                  <a href='/searchTransactions'>Search Transactions</a>|\
                                  <a href='/allTransactions'>All Transactions</a>|\
                                  <a href='/deleteAccount'>Delete Account</a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Amount $")
                self.wfile.write(str(amount).encode())
                self.wfile.write(b" has been withdrawn")
                self.wfile.write(b" from account ID: ")
                self.wfile.write(str(accountId).encode())
                self.wfile.write(b"</h3>")

                self.wfile.write(b"<div><a href='/withdraw'>Withdraw again</a></div>")
                self.wfile.write(b"</center></body></html>")

            elif self.path == '/deposit':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                accountId = int(form.getvalue("accountId"))
                amount    = float(form.getvalue("amount"))

                self.database.deposit(accountId,amount)
                print("grabbed values",accountId, amount)

                self.wfile.write(b"<html><head><title> Bank's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Bank's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addAccount'>Add Account</a>|\
                                  <a href='/withdraw'>Withdraw</a>|\
                                  <a href='/deposit'>Deposit </a>|\
                                  <a href='/searchTransactions'>Search Transactions</a>|\
                                  <a href='/allTransactions'>All Transactions</a>|\
                                  <a href='/deleteAccount'>Delete Account</a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Amount $")
                self.wfile.write(str(amount).encode())
                self.wfile.write(b" has been deposited into account ID: ")
                self.wfile.write(str(accountId).encode())
                self.wfile.write(b"</h3>")
                self.wfile.write(b"<div><a href='/deposit'>Deposit again</a></div>")
                self.wfile.write(b"</center></body></html>")
            elif self.path == '/searchTransactions':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                accountId = int(form.getvalue("accountId"))

                ##Call the Database Method to a add a new student
                '''
                    Example call: self.database.addAccount(student_name, ownerName, owner_ssn, balance, status)
                '''

                print("grabbed values",accountId)

                data=[]
                records = self.database.accountTransactions(accountId)
                print(records)
                data=records
                self.wfile.write(b"<html><head><title> Bank's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Bank's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addAccount'>Add Account</a>|\
                                  <a href='/withdraw'>Withdraw</a>|\
                                  <a href='/deposit'>Deposit </a>|\
                                  <a href='/searchTransactions'>Search Transactions</a>|\
                                  <a href='/allTransactions'>All Transactions</a>|\
                                  <a href='/deleteAccount'>Delete Account</a></div>")
                self.wfile.write(b"<hr><h2>Transactions for account ID: ")
                self.wfile.write(str(accountId).encode())
                self.wfile.write(b"</h2>")
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Transaction ID </th>\
                                        <th> Account ID</th>\
                                        <th> Transaction Type</th>\
                                        <th> Amount </th></tr>")
                for row in data:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td></tr>')

                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return
            elif self.path == '/deleteAccount':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                accountId = int(form.getvalue("accountId"))

                self.database.deleteAccount(accountId)
                print("grabbed values",accountId)

                self.wfile.write(b"<html><head><title> Bank's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Bank's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addAccount'>Add Account</a>|\
                                  <a href='/withdraw'>Withdraw</a>|\
                                  <a href='/deposit'>Deposit </a>|\
                                  <a href='/searchTransactions'>Search Transactions</a>|\
                                  <a href='/allTransactions'>All Transactions</a>|\
                                  <a href='/deleteAccount'>Delete Account</a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Account ID: ")
                self.wfile.write(str(accountId).encode())
                self.wfile.write(b" has been deleted")
                self.wfile.write(b"</h3>")

                self.wfile.write(b"<div><a href='/deleteAccount'>Delete another account</a></div>")
                self.wfile.write(b"</center></body></html>")


        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)


        return

    ''' Function to handle GET request which happen after we click on a link'''
    def do_GET(self):
        try:
            if self.path == '/': #This code generates the home page
                data=[]
                records = self.database.getAllAccounts() #Calls this function from portalDatabase.py
                print(records)
                data=records

                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Bank's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Bank's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addAccount'>Add Account</a>|\
                                  <a href='/withdraw'>Withdraw</a>|\
                                  <a href='/deposit'>Deposit </a>|\
                                  <a href='/searchTransactions'>Search Transactions</a>|\
                                  <a href='/allTransactions'>All Transactions</a>|\
                                  <a href='/deleteAccount'>Delete Account</a></div>")
                self.wfile.write(b"<hr><h2>All Accounts</h2>")
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Account ID </th>\
                                        <th> Account Owner</th>\
                                        <th> Balance </th>\
                                        <th> Status </th></tr>")
                for row in data: # We go through each account returned and show them as rows of table here
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td></tr>')

                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return
            if self.path == '/addAccount': #This code handles the request when we click on Add Account
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Bank's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Bank's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addAccount'>Add Account</a>|\
                                  <a href='/withdraw'>Withdraw</a>|\
                                  <a href='/deposit'>Deposit </a>|\
                                  <a href='/searchTransactions'>Search Transactions</a>|\
                                  <a href='/allTransactions'>All Transactions</a>|\
                                  <a href='/deleteAccount'>Delete Account</a></div>")
                self.wfile.write(b"<hr><h2>Add New Account</h2>")

                self.wfile.write(b"<form action='/addAccount' method='post'>")
                self.wfile.write(b'<label for="oname">Owner Name:</label>\
                      <input type="text" id="oname" name="oname"><br><br>\
                      <label for="owner_ssn">Owner SSN:</label>\
                      <input type="number" id="owner_ssn" name="owner_ssn"><br><br>\
                      <label for="balance">Balance:</label>\
                      <input type="number" step="0.01" id="balance" name="balance"><br><br>\
                      <input type="submit" value="Submit">\
                      </form>')

                self.wfile.write(b"</center></body></html>")
                return
            if self.path == '/withdraw': #This code receives the GET request when we click on the Withdraw link
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Bank's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Bank's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addAccount'>Add Account</a>|\
                                  <a href='/withdraw'>Withdraw</a>|\
                                  <a href='/deposit'>Deposit </a>|\
                                  <a href='/searchTransactions'>Search Transactions</a>|\
                                  <a href='/allTransactions'>All Transactions</a>|\
                                  <a href='/deleteAccount'>Delete Account</a></div>")
                self.wfile.write(b"<hr><h2>Withdraw from an account</h2>")
                self.wfile.write(b"<form action='/withdraw' method='post'>")
                self.wfile.write(b'<label for="accountId">Account ID:</label>\
                      <input type="number" id="accountId" name="accountId"><br><br>\
                      <label for="amount">Amount:</label>\
                      <input type="number" step="0.01" id="amount" name="amount"><br><br>\
                      <input type="submit" value="Submit">\
                      </form>')
                self.wfile.write(b"</center></body></html>")
                return

            if self.path =='/deposit':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Bank's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Bank's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addAccount'>Add Account</a>|\
                                  <a href='/withdraw'>Withdraw</a>|\
                                  <a href='/deposit'>Deposit </a>|\
                                  <a href='/searchTransactions'>Search Transactions</a>|\
                                  <a href='/allTransactions'>All Transactions</a>|\
                                  <a href='/deleteAccount'>Delete Account</a></div>")
                self.wfile.write(b"<hr><h2>Deposit into an account</h2>")
                self.wfile.write(b"<form action='/deposit' method='post'>")
                self.wfile.write(b'<label for="accountId">Account ID:</label>\
                      <input type="number" id="accountId" name="accountId"><br><br>\
                      <label for="amount">Amount:</label>\
                      <input type="number" step="0.01" id="amount" name="amount"><br><br>\
                      <input type="submit" value="Submit">\
                      </form>')
                self.wfile.write(b"</center></body></html>")
                return
            if self.path =='/searchTransactions':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Bank's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Bank's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addAccount'>Add Account</a>|\
                                  <a href='/withdraw'>Withdraw</a>|\
                                  <a href='/deposit'>Deposit </a>|\
                                  <a href='/searchTransactions'>Search Transactions</a>|\
                                  <a href='/allTransactions'>All Transactions</a>|\
                                  <a href='/deleteAccount'>Delete Account</a></div>")
                self.wfile.write(b"<hr><h2>Search Transactions</h2>")
                self.wfile.write(b"<form action='/searchTransactions' method='post'>")
                self.wfile.write(b'<label for="accountId">Account ID:</label>\
                      <input type="number" id="accountId" name="accountId"><br><br>\
                      <input type="submit" value="Submit">\
                      </form>')
                self.wfile.write(b"</center></body></html>")


            if self.path =='/deleteAccount':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Bank's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Bank's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addAccount'>Add Account</a>|\
                                  <a href='/withdraw'>Withdraw</a>|\
                                  <a href='/deposit'>Deposit </a>|\
                                  <a href='/searchTransactions'>Search Transactions</a>|\
                                  <a href='/allTransactions'>All Transactions</a>|\
                                  <a href='/deleteAccount'>Delete Account</a></div>")
                self.wfile.write(b"<hr><h2>Delete Account</h2>")
                self.wfile.write(b"<form action='/deleteAccount' method='post'>")
                self.wfile.write(b'<label for="accountId">Account ID:</label>\
                      <input type="number" id="accountId" name="accountId"><br><br>\
                      <input type="submit" value="Submit">\
                      </form>')
                self.wfile.write(b"</center></body></html>")

            if self.path == '/allTransactions':
                data=[]
                records = self.database.getAllTransactions()
                print(records)
                data=records

                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Bank's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Bank's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addAccount'>Add Account</a>|\
                                  <a href='/withdraw'>Withdraw</a>|\
                                  <a href='/deposit'>Deposit </a>|\
                                  <a href='/searchTransactions'>Search Transactions</a>|\
                                  <a href='/allTransactions'>All Transactions</a>|\
                                  <a href='/deleteAccount'>Delete Account</a></div>")
                self.wfile.write(b"<hr><h2>All Transactions</h2>")
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Transaction ID </th>\
                                        <th> Account ID</th>\
                                        <th> Transaction Type </th>\
                                        <th> Amount </th></tr>")
                for row in data:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td></tr>')

                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return

        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)



def run(server_class=HTTPServer, handler_class=PortalRequestHandler, port=8000):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port {}'.format(port))
    httpd.serve_forever()

run()
