# This is a simple bank account simulator that allows users to create an account, deposit money, withdraw money, and check their balance.

#use constants
#explain why the code is used

from tkinter import *
from tkinter import messagebox
import matplotlib

#initial balance, set at 0 as there is no accounts yet
balance = 0
transaction_histroy = []
amount = 0

#function for withdrawing money
def withdraw(balance,amount):
    while True:
        try:
            amount = int(input("Enter amount to withdraw: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
    if amount > balance:
        print("Insufficient funds")
    else:
        balance -= amount
        transaction_histroy.append(f"Withdrew {amount}")
    return balance

        
        
#function for depositing money
def deposit(balance):
    while True:
        try:
            amount = int(input("Enter amount to deposit: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    balance += amount
    transaction_histroy.append(f"Deposited {amount}")
    return balance
    
def user_balance(balance):
    print("Your balance is: ", balance)

def user_histroy():
    print("Transaction history: ")
    for transaction in transaction_histroy:
        print(transaction)

#selecting users action
print("create your account")
account_name = input("Enter your name: ")
while True:
    print(f"account name: {account_name}")
    user_balance(balance)
    user_action = input("Enter 'd' to deposit, 'w' to withdraw, or 'h' balance_history, or 'e' to exit: ").lower()
    if user_action == 'd': 
        balance = deposit(balance)
    elif user_action == 'w':
        balance = withdraw(balance,amount)
    elif user_action == 'h':
        user_histroy()
    elif user_action == 'e':
        break
    else:
        print("Invalid action")
 