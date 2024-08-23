import json
from datetime import datetime
import os
from math import ceil
TRANSACTIONS = 'transactions.json'

def intro():
    print("-----------------------------")
    print("Welcome to our Banking System")
    print("-------------------------------")
    LogInOrSignUp()

def menuForUser(account_number):
    print("---------------------------------------")
    print("Welcome to the main menu of our Bank")
    print("What operation do you want to do?")
    print("1. Transact\n2. Balance Check\n3. User Data Change\n4. Loan management")
    print("----------------------------------------")
    user_second_input = int(input())
    if user_second_input == 2:
        check_balance(account_number)
    elif user_second_input == 1:
        transactions(account_number)
    elif user_second_input == 3:
        changeData()    
    else:
        loan_management()    

def loan_management():
    print("To take a loan press 1, To see info about current loan press 2")
    loan_input = int(input())
    if loan_input == 2:
        print("------------------------")
        print("Enter your loan amount")
        print("------------------------")
        loan = int(input())
        print("------------------------")
        print("Enter the percent of your loan")
        print("------------------------")
        percent = int(input())
        print("------------------------")
        print("Enter you monthly payment")
        print("------------------------")
        monthly = int(input())
        result = calculate_loan_duration(loan, percent, monthly)
        print(f"You gotta pay it in {result} months")
    else:
        print("------------------")
        print("Enter the amount")
        print("------------------")
        ltk = int(input())
        print("------------------")
        print("Enter the interest rate")
        print("------------------")
        ir = int(input())
        print("------------------")
        print("Enter the duration")
        print("------------------")
        mp = int(input())
        print(f"Your monthly payment will be {calculate_monthly_payment}")


def calculate_monthly_payment(loan_amount, annual_interest_rate, duration_in_months):
    if duration_in_months <= 0:
        return "Duration must be greater than 0."
    
    monthly_interest_rate = annual_interest_rate / 12 / 100
    
    if monthly_interest_rate == 0:  # Special case for 0% interest
        return loan_amount / duration_in_months
    
    numerator = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** duration_in_months
    denominator = (1 + monthly_interest_rate) ** duration_in_months - 1
    
    monthly_payment = numerator / denominator
    
    return round(monthly_payment, 2)

# Example usage
loan_amount = 10000  # Example loan amount
annual_interest_rate = 5  # Example interest rate
duration_in_months = 60  # Example duration in months

monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, duration_in_months)
print(f"The monthly payment is ${monthly_payment}.")

    
def calculate_loan_duration(loan_amount, annual_interest_rate, monthly_payment):
    if monthly_payment <= 0:
        return "Monthly payment must be greater than 0."

    monthly_interest_rate = annual_interest_rate / 12 / 100
    months = 0

    while loan_amount > 0:
        loan_amount += loan_amount * monthly_interest_rate
        
        loan_amount -= monthly_payment
        
        months += 1

        if months > 600:  
            return "Loan cannot be paid off with the current payment."

    return months

def changeData():
    print("please enter your account number")
    ac_number = input()
    
    data = load_data()
    account = find_account(ac_number, data)
    
    if account is None:
        print("Account not found")
        return
    
    print("---------------------------------------")
    print("1. Add Phone Number\n2. Add Address\n3. Change Password")
    print("---------------------------------------")
    
    user_answer = int(input())
    
    if user_answer == 1:
        print("Please enter your phone number")
        account['phone_number'] = input()
        print("Phone number added successfully")
    
    elif user_answer == 2:
        print("Please enter your address")
        account['address'] = input()
        print("Address added successfully")
    
    elif user_answer == 3:
        print("Please enter your old password")
        old_password = input()
        if account['password'] == old_password:
            print("Enter your new password")
            new_password = input()
            print("Confirm your new password")
            confirm_password = input()
            if new_password == confirm_password:
                account['password'] = new_password
                print("Password changed successfully")
            else:
                print("Passwords do not match")
        else:
            print("Incorrect old password")
    
    save_data(data)

                




def log_transaction(transaction):
    data = load_transactions()
    data["transactions"].append(transaction)
    save_transactions(data)

def transactions(user_acc):
    data = load_data()
    
    print("Please enter the account number you want to send money to:")
    send_to = input().strip()
    
    print("How much money do you want to transact?")
    money = float(input().strip())

    sender_account = find_account(user_acc, data)
    receiver_account = find_account(send_to, data)

    if sender_account is None:
        print("Sender account not found.")
        return
    if receiver_account is None:
        print("Receiver account not found.")
        return

    if sender_account['balance'] < money:
        print("Insufficient balance.")
        return
    
    if sender_account['card_type'] == receiver_account['card_type']:
        sender_account['balance'] -= money
        receiver_account['balance'] += money
    else:
        moneyToSend = 0.95 * money
        sender_account['balance'] -= moneyToSend
        receiver_account['balance'] += moneyToSend    

    

    transaction = {
        "date": datetime.now().isoformat(),
        "from_account": user_acc,
        "to_account": send_to,
        "amount": money
    }

    sender_account['transactions'].append(transaction)
    receiver_account['transactions'].append(transaction)

    save_data(data)
    log_transaction(transaction)

    print(f"Transaction successful! ${money} has been sent from account {user_acc} to account {send_to}.")

def find_account(account_number, data):
    for account in data['users']:
        if account['account_number'] == account_number:
            return account
    return None

def LogInOrSignUp():
    print("If you have an account press 1 else press 2")
    user_input = int(input())
    if user_input == 1:
        print("Please enter your account number and password")
        input_line = input().strip()
        account_number, password = input_line.split(maxsplit=1)
        if user_exists(account_number, password):
            menuForUser(account_number)
        else:
            print("Login failed. Please try again.")
    else:
        print("Please enter your name:")
        name = input().strip()
        print("Please enter a password:")
        password = input().strip()
        create_account(name, password)

def load_data(file_path='users.json'):
    absolute_path = os.path.abspath(file_path)
    print(f"Attempting to load data from: {absolute_path}")
    try:
        with open(absolute_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {absolute_path}")
        return {"users": []}
    except json.JSONDecodeError:
        print("Error decoding JSON. The file might be corrupted.")
        return {"users": []}


def save_data(data, file_path='users.json'):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def create_account(name, password):
    data = load_data()
    new_account = {
        "account_number": str(len(data["users"]) + 1).zfill(6),  # Simple unique account number
        "name": name,
        "balance": 0.0,
        "password": password,
        "transactions": []
    }
    data["users"].append(new_account)
    save_data(data)
    print(f"Account created for {name}. Account number: {new_account['account_number']}")

def check_balance(account_number):
    data = load_data()
    for account in data["users"]:
        if account["account_number"] == account_number:
            print(f"Account Balance for {account['name']}: ${account['balance']}")
            return
    print("Account not found.")

def user_exists(account_number, password):
    data = load_data()
    for account in data["users"]:
        if account["account_number"] == account_number and account["password"] == password:
            print(f"User {account['name']} authenticated successfully.")
            return True
    print("Authentication failed. Account number or password is incorrect.")
    return False

def load_transactions(file_path=TRANSACTIONS):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"transactions": []}

def save_transactions(data, file_path=TRANSACTIONS):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

intro()
