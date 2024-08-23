Banking System Project
This project is a simple console-based Banking System implemented in Python. It allows users to manage their bank accounts, perform transactions, check their balance, change user data, and manage loans.

Features
User Authentication:

Log in or sign up for an account.
Each user is assigned a unique account number.
Transaction Management:

Perform transactions between accounts.
Log all transactions with details like date, sender, receiver, and amount.
Handle transactions between different card types with a 5% fee.
Balance Check:

Easily check the balance of an account.
User Data Management:

Update user information such as phone number, address, and password.
Loan Management:

Calculate the monthly payment for a loan based on the amount, interest rate, and duration.
Calculate the duration required to pay off a loan based on the monthly payment, loan amount, and interest rate.
Data Persistence:

User data is stored in a JSON file (users.json).
Transaction records are stored in a separate JSON file (transactions.json).


How It Works
The system prompts the user to either log in or sign up for a new account.
After logging in, the user can choose from several options: perform a transaction, check balance, change user data, or manage loans.
The system ensures that transactions are logged and balances are updated accurately.
User and transaction data are persisted in JSON files, making the system's state consistent across sessions.
Future Enhancements
Implementing additional security measures like encryption for storing passwords.
Expanding loan management with more complex interest rate calculations and repayment options.
Adding more banking features such as bill payments, fund transfers, and account statements.
Introducing a graphical user interface (GUI) to enhance user experience.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an issue for suggestions.

Author
Armen-Aris Shahinyan
