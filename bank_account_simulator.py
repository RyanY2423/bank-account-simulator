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
deposit_amount = 0


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
def deposit():

    #sets up the label and entry box for the deposits
    deposit_amounts = Entry()
    deposit_amounts.grid(row=2, column=0, padx=10, pady=10,columnspan=4,)
    amount_label = Label(root, text="Enter amount to deposit: ")
    amount_label.grid(row=1, column=0, padx=10, pady=10,columnspan=4)
    submit_button = Button(root, text="Submit", command=lambda: deposit_submit(deposit_amounts,amount_label,submit_button))
    submit_button.grid(row=3, column=0, padx=10, pady=10,columnspan=4)



#function to submit deposit 
def deposit_submit(deposit_amounts,amount_label,submit_button):
    global balance
    try:
        #checks if the deposit amount is a number
        deposit_amount = int(deposit_amounts.get())
        if deposit_amount < 0:
            #if the amount is negative it will give an error
            raise ValueError
        balance += int(deposit_amount)
        transaction_histroy.append(f"Deposited {deposit_amount}")
        shown_balance.config(text=f"Your balance is: ${balance}")
        #removing the deposit amount entry and label
        deposit_amounts.destroy()  
        amount_label.destroy()  
        submit_button.destroy() 
        label.config(text="deposit succesful",fg="black")
    except ValueError:
        label.config(text="Invalid input. Please enter a valid number.")


#function to submiot withdraw
def withdraw_submit(withdraw_amount):
    global balance
    balance -= int(deposit_amount.get())
    if balance < 0:
        label.config(text="Insufficient funds")
    print(balance)
    print(f"Deposited {deposit_amount.get()}")
    transaction_histroy.append(f"Deposited {deposit_amount.get()}")
    shown_balance.config(text=f"Your balance is: ${balance}")



    
#function to show the balance    
def user_balance(balance):
    print("Your balance is: ", balance)

#function to show the transaction history
def user_histroy():
    print("Transaction history: ")
    for transaction in transaction_histroy:
        print(transaction)

#main program
#creating a window
root = Tk()
root.title("Bank Account Simulator")
root.geometry("800x600")


#creating labels for the main page

shown_balance = Label(root, text=f"your balance is: ${balance}")
shown_balance.grid(row=0, column=0, padx=5, pady=10,columnspan=4)
label = Label(root, text=f"",fg="red")
label.grid(row=1, column=0, padx=5, pady=10,columnspan=4,rowspan=2)

#buttons for user actions
#deposit
deposit_button = Button(root, text="Deposit", command=lambda:deposit())
deposit_button.grid(row=4, column=0, padx=5, pady=10)
#withdraw
withdraw_button = Button(root, text="Withdraw", )
withdraw_button.grid(row=4, column=1, padx=5, pady=10)
#transaction history
history_button = Button(root, text="History", )
history_button.grid(row=4, column=2, padx=5, pady=10)

#button to quit the program
close = Button(root, text="Close", command=root.quit)
close.grid(row=4, column=3, padx=5, pady=10)


#running the main loop
root.mainloop()



