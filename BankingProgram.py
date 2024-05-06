#This is a banking program with different features for both customers and admins. There are many different functions including storing the data within a file in order to ensure data permanence,
#withdrawing and depositing, and even using object stored lists in order to output data and save it.

class BankAccount:
    def __init__(self, accountNumber, balance, accountType):
        self.accountNumber = accountNumber
        self.balance = float(balance)
        self.accountType = accountType
    def __str__(self):
        #outputs information about the bank account given
        return f"Account Number: {self.accountNumber}, Balance: {self.balance}, Account Type: {self.accountType}"
    

    def deposit(self, deposit_amount, enteredUserName):
        #allows the user to deposit cash, outputs the old amount and new amount, and then updates the amount in the file.
        print(f"Your original balance was: ${self.balance}")
        deposit_amount = float(deposit_amount) 
        self.balance += deposit_amount
        self.balance = '{:.2f}'.format(self.balance)
        print(f"Your balance is now at: ${self.balance}")

        createNewDepositTransaction(deposit_amount, enteredUserName)

        overwriteBalance(enteredUserName)
        
        return self.balance
    def withdraw(self, withdraw_amount, enteredUserName):
        #allows the user to withdraw cash, outputs the old amount and new amount, and then updates the amount in the file.


        print(f"Your original balance was: ${self.balance}")
        self.balance -= withdraw_amount
        self.balance = '{:.2f}'.format(self.balance)
        print(f"Your balance is now at: ${self.balance}")
        createNewWithdrawTransaction(withdraw_amount, enteredUserName)
        overwriteBalance(enteredUserName)

        return self.balance
    
    def viewBalance(self):
        #allows user to view their current balance
        self.balance = '{:.2f}'.format(self.balance)
        print(f"Your total balance today is: {self.balance}")
        return 
    
class Customer:
    def __init__(self, firstName, lastName, username, password, age, email, accountType, accountNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.password = password
        self.age = age
        self.email = email
        self.accountType = accountType
        self.accountNumber = accountNumber
    def __str__(self):
        #outputs information about customer
        return f"Customer: {self.firstName} {self.lastName}, Username: {self.username}, Age: {self.age}, Email: {self.email}, Account Type: {self.accountType}, Account Number: {self.accountNumber}"
class Bank:
    def __init__(self, bankName, location):
        self.bankName = bankName
        self.location = location
        self.interestRates = {'savings' : 0.05,
                              'checkings' : 0.01}
                              
        self.transactionHistory = []
    def viewTransactionHistory(self):
        #prints the entirety of the transaction history from a file

        for transaction in transactions:
            print(transaction)

        self.transactionHistory.append(transactions)
    
    def viewInterestRates(self):
        #prints the interest rates of the bank, different for savings and checkings accounts
        import json
        json_str = json.dumps(bank.interestRates, indent = 4)

        print(json_str)

            
        


customers = []
accounts = []
transactions = []


def createNewDepositTransaction(deposit_amount, enteredUserName):
    #saves deposit transaction to a list
    transactions.append(f"Username - '{enteredUserName}' Deposit amount - ${deposit_amount}")
    saveTransaction(enteredUserName, deposit_amount)

def createNewWithdrawTransaction(withdraw_amount, enteredUserName):
    #saves withdraw transaction to a list
    transactions.append(f"Username - '{enteredUserName}' Withdraw amount - ${withdraw_amount}")
    saveTransaction(enteredUserName, withdraw_amount)

def saveTransaction(enteredUserName, deposit_amount):
    #saves transactions to a file to keep for future program runs.
    with open("transactionhistory.txt", 'a') as file:
        file.write(f"{enteredUserName},{deposit_amount}\n")

def loadTransactions():

    #loads past transactions from transactionhistory.txt
    with open("transactionhistory.txt", 'r') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            data = line.strip().split(',')

            enteredUserName, deposit_amount = data
            transactions.append(f"Username - '{enteredUserName}' amount - ${deposit_amount}")


def quit():
    import sys
    print("Shutting down...")
    sys.exit()

def customerLogin():

    #checks to ensure we have a saved username following what they enter, along with password

    enteredUserName = input("Please enter your username: ").lower()

    if enteredUserName == 'quit':
        quit()

    targetCustomer = None
    while targetCustomer == None:

        for customer in customers:
            if enteredUserName == customer.username.lower():
                targetCustomer = customer
                break
        else:
            enteredUserName = input("Invalid username, try again or enter 'quit' to quit: ")
            if enteredUserName == 'quit':
                quit()

    print("-----------------------------")
    enteredPassword = input("Please enter your password: ")

    if enteredPassword == 'quit':
        quit()

    for customer in customers:
        if enteredPassword == customer.password:
            targetCustomer = customer
            break
    else:
        enteredUserName = input("Invalid password, try again or enter 'quit' to quit: ")
        if enteredUserName == 'quit':
            quit()
    print("Correct password!\nLogging in...")

    customerChoices(enteredUserName)


def adminPage():
    #display options for admin, ensuring entered variable is an int. 

    adminOptions = ["View Transaction History", "Remove User", "View a list of all users", "View interest rates: "]
    print("Enter the number corresponding with the action you would like to perform - ")


    adminChoice = checkIfInt(f"1 - {adminOptions[0]} - 2 - {adminOptions[1]} - 3 - {adminOptions[2]} - 4 - {adminOptions[3]}")

    if int(adminChoice) == 1:
        bank.viewTransactionHistory()
    elif int(adminChoice) == 2:
        removeUser()
    elif int(adminChoice) == 3:
        viewAllUsers()
    elif int(adminChoice) == 4:
        bank.viewInterestRates()
    else:
        print("Invalid entry...")
        quit()
    
def removeUser():
    #prompts the user to enter the username of the user they want to delete, and removes from the file along with the list.

    for customer in customers:
        print(customer)
    userToRemove = input("Enter username of user you want to remove from the list: ")

    for customer in customers:
        if userToRemove == customer.username:
            customers.remove(customer)
            with open("bankingdata.txt", 'r') as file:
                
                lines = file.readlines()
                modified_lines = [line for line in lines if userToRemove not in line.strip()]

            with open("bankingdata.txt", 'w') as file:
                file.writelines(modified_lines)
            break
    else:
        print("Invalid user entered")
        quit()
    
    print(userToRemove + " removed.")

def viewAllUsers():
    #prints a list out of all users
    totalCount = 0
    for customer in customers:
        print(customer)
        totalCount += 1
    print("Total amount of customers: " + str(totalCount))


def customerChoices(enteredUserName):
    #prints out customer choices and brings them to that choice accordingly.

    targetCustomer = None
    for customer in customers:
        if enteredUserName.lower() == customer.username.lower():
            targetCustomer = customer
            break

    print(f"Welcome {enteredUserName}, what would you like to do today (enter 0 to quit)?: ")
    choices = ["Deposit", "Withdraw", "View Balance", "Loan Calculator"]
    while True:
        customerInput = checkIfInt(f"1 - {choices[0]} - 2 - {choices[1]} - 3 - {choices[2]} - 4 - {choices[3]}: ")
        try:
            customerInput = int(customerInput)
            if 1 <= customerInput <= len(choices):
                break
            else:
                print("Invalid choice. Please enter a number corresponding to the given options.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    customerAccount = None
    for account in accounts:
        if account.accountNumber == targetCustomer.accountNumber:
            customerAccount = account
            break
    if customerAccount is None:
        print("Account not found.")
        quit()
    
   
    if int(customerInput) == 1:
        deposit_amount = float(input("Enter the deposit amount: "))
        customerAccount.deposit(deposit_amount, enteredUserName)
    elif int(customerInput) == 2:
        withdraw_amount = float(input("Enter the withdrawal amount: "))
        customerAccount.withdraw(withdraw_amount, enteredUserName)
    elif int(customerInput) == 3:
        customerAccount.viewBalance()
    elif int(customerInput) == 4:
        loanCalc(enteredUserName)
    elif int(customerInput) == 0:
        quit()
    else:
        print("Invalid input.")
        quit()

def findCustomer(enteredUserName):

    #sorts through list of customer objects in order to find the correct customer, along with their account number
    targetCustomer = None
    for customer in customers:
        if enteredUserName.lower() == customer.username.lower():
            targetCustomer = customer
            break
    customerAccount = None
    for account in accounts:
        if account.accountNumber == targetCustomer.accountNumber:
            customerAccount = account
            break
    if customerAccount is None:
        print("Account not found.")
        quit()
    return account

def loanCalc(enteredUserName):

    #calculates the total cost after interest, what their interest rate will be, and how much in pure interest they have paid.
    targetCustomer = None
    for customer in customers:
        if enteredUserName.lower() == customer.username.lower():
            targetCustomer = customer
            break
    customerAccount = None

    loanAmount = input("How much money would you like a loan of?: ")

    yearCount = input("How many years would you be taking the loan out for?: ")

    if int(yearCount) in range(0,2):
        percentage = 0.10
    elif int(yearCount) in range(2,4):
        percentage = 0.07
    elif int(yearCount) in range(4,9):
        percentage = 0.05
    elif int(yearCount) >= 9:
        percentage = 0.03

    loanAmount = float(loanAmount)
    yearCount = float(yearCount)
    percentage = float('{:.2f}'.format(percentage))

    print(f"Your interest rate is going to be: {percentage*100}%")
    percentage = float(percentage)
    
    totalInterest = loanAmount * percentage * yearCount
    totalPaid = loanAmount + totalInterest
    print(f"The total cost after interest will be: ${totalPaid}")
    print(f"The total amount of interest will be: ${totalInterest}")

    print("--------------------------------\n")

    customerChoices(enteredUserName)

def checkIfInt(enter):
    #checks if the entered value is of type int.
    while True:
        user_input = input(enter)
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer.")


def createNewAccount():
    #creates new account, of which is then saved to a file and list

    customerFirstName = input("Enter your first name: ")
    customerLastName = input("Enter your last name: ")
    newUserName = input("Enter the desired username: ")
    newPassword = input("Enter your desired password (must be at least 4 characters): ")
    letterCount = 0
    for char in newPassword:
        letterCount += 1
    
    while letterCount < 4:
        newPassword = input("You need at least 4 characters, try again: ")
        letterCount = 0
        for char in newPassword:
            letterCount += 1

    age = input("Enter your age: ")
    if int(age) < 18:
        print("Invalid age...")
        sys.exit()

    email = input("Enter your email: ")
    while '@' not in email:
        while '.com' not in email:
            email = input("Invalid email address, try again (include '@' and '.com'): ")

    accountType = input("Enter the wanted type of bank account (checkings) or (savings): ").lower()
    while accountType not in ['checkings', 'savings']:
        accountType = input("Invalid account type, please try again: ")

    accountNumber = getAccountNumber()
    print("Your account number will be: " + str(accountNumber))

    balance = input("Please enter your initial deposit: ($1.00 minimum): ")


    storeData(customerFirstName, customerLastName, newUserName, newPassword, age, email, accountType, accountNumber, balance)

def getAccountNumber():

    #randomly generates a new account number that is assigned to a new user
    import random
    accountNumber = random.randint(1000,1000000)
    return accountNumber

def storeData(customerFirstName, customerLastName, newUserName, newPassword, age, email, accountType, accountNumber, balance):

    #saves data of customers along with their balance into a file, as well as a list
    with open("bankingdata.txt", 'a') as file:
        file.seek(0)

        data = f"{customerFirstName},{customerLastName},{newUserName},{newPassword},{age},{email},{accountType},{accountNumber},{balance}\n"
        file.write(data)
    balance = float(balance)
    balance = '{:.2f}'.format(balance)

    customers.append(Customer(customerFirstName, customerLastName, newUserName,newPassword,age,email,accountType,accountNumber))
    accounts.append(BankAccount(accountNumber, balance, accountType))

    print(f"You entered: {data}")
        
        
def loadData():

    #We load the information from the bankingdata.txt file in order to create a list of objects and save data through different sessions.

    with open("bankingdata.txt", 'r') as file:
        lines = file.readlines()
        file.seek(0)

        for line in lines:
            data = line.strip().split(',')
            firstName, lastName, newUserName, newPassword, age, email, accountType, accountNumber, balance = data 
            customers.append(Customer(firstName, lastName, newUserName, newPassword, age, email, accountType, accountNumber))
            accounts.append(BankAccount(accountNumber, balance, accountType))


def overwriteBalance(enteredUserName):
    #overwrites the previous balance with the new balance after a transaction
    account = findCustomer(enteredUserName)

    with open("bankingdata.txt", 'r+') as file:
        lines = file.readlines()
        file.seek(0)

        for index, line in enumerate(lines):
            data = line.strip().split(',')
            if enteredUserName.lower() == data[2].lower():
                data[8] = str(account.balance) 
                lines[index] = ','.join(data) + '\n'
                file.writelines(lines)  
                break

def mainMenu():
    #greets the user and allows them to enter different options, if 'Admin123' is entered, it asks for the Admin password and then brings them to the Admin menu.
    userInput = input("Welcome to Evergreen Financial Services \nEnter 'login' to login, or enter 'New User' in order to create a new account: ")
    if userInput == "Admin123":
        password = 123
        passwordEntered = input("Enter admin password: ")

        while int(passwordEntered) != password:
                
            passwordEntered = input("Invalid input, try again or 999 to exit: ")
            if int(passwordEntered) == 999:
                quit()

        print("Welome admin...")
        adminPage()
    elif userInput == "New User":
        createNewAccount()
    elif userInput.lower() == "login":
        customerLogin()
    else:
        print("Invalid entry...")

loadData()
loadTransactions()
bank = Bank("Evergreen Financial Services", "Colorado")
mainMenu()
