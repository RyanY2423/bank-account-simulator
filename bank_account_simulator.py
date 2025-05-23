# This is a simple bank account simulator that allows users to create an account, deposit money, withdraw money, and check their balance.

#explain why the code is used

from tkinter import *
from tkinter import messagebox
import matplotlib

#initial balance, set at 0 as there is no accounts yet
balance = 0
transaction_histroy = []
amount = 0
deposit_amount = 0


#function for depositing money
def deposit():
    #deletes inputs for withdraw to prevent overlapping	
    deposit_button.grid_forget()
    withdraw_button.grid_forget()
    history_button.grid_forget()
    cancel_button = Button(root, text="Cancel", command=lambda:cancel(entered_amounts,amount_label,submit_button,cancel_button))
    cancel_button.grid(row=4, column=1, padx=5, pady=10)
    #sets up the label and entry box for the deposits
    entered_amounts = Entry()
    entered_amounts.grid(row=2, column=0, padx=10, pady=10,columnspan=4,)
    amount_label = Label(root, text="Enter amount to deposit: ")
    amount_label.grid(row=1, column=0, padx=10, pady=10,columnspan=4)
    submit_button = Button(root, text="Submit", command=lambda: deposit_submit(entered_amounts,amount_label,submit_button,cancel_button))
    submit_button.grid(row=3, column=0, padx=10, pady=10,columnspan=4)



#function to submit deposit 
def deposit_submit(entered_amounts,amount_label,submit_button,cancel_button):
    global balance
    try:
        #checks if the deposit amount is a number
        deposit_amount = int(entered_amounts.get())
        if deposit_amount < 0:
            #if the amount is negative it will give an error
            raise ValueError
        balance += int(deposit_amount)
        transaction_histroy.append(f"Deposited {deposit_amount}")
        shown_balance.config(text=f"Your balance is: ${balance}")
        #removing the deposit amount entry and label
        entered_amounts.destroy()  
        amount_label.destroy()  
        submit_button.destroy() 
        label.config(text="deposit succesful",fg="black")
        #returning the buttons
        deposit_button.grid(row=4, column=0, padx=5, pady=10)
        withdraw_button.grid(row=4, column=1, padx=5, pady=10)
        history_button.grid(row=4, column=2, padx=5, pady=10)
        cancel_button.destroy()
    except ValueError:
        label.config(text="Invalid input. Please enter a valid number.")


#function for withdrawing money
def withdraw():
    #deletes inputs for deposit to prevent overlapping
    deposit_button.grid_forget()
    withdraw_button.grid_forget()
    history_button.grid_forget()
    #sets up the label and entry box for the withdraw
    entered_amounts = Entry()
    entered_amounts.grid(row=2, column=0, padx=10, pady=10,columnspan=4,)
    amount_label = Label(root, text="Enter amount to withdraw: ")
    amount_label.grid(row=1, column=0, padx=10, pady=10,columnspan=4)
    submit_button = Button(root, text="Submit", command=lambda: withdraw_submit(entered_amounts,amount_label,submit_button,cancel_button))
    submit_button.grid(row=3, column=0, padx=10, pady=10,columnspan=4)
    cancel_button = Button(root, text="Cancel", command=lambda:cancel(entered_amounts,amount_label,submit_button,cancel_button))
    cancel_button.grid(row=4, column=1, padx=5, pady=10)


#function to submiot withdraw
def withdraw_submit(entered_amounts,amount_label,submit_button,cancel_button):
    global balance
    try:
    #checks if the deposit amount is a number
        withdraw_amount = int(entered_amounts.get())
        if withdraw_amount < 0:
            #if the amount is negative it will give an error
            raise ValueError
        elif withdraw_amount > balance:
            #if the amount is more than the balance it will give an error
            raise ValueError
        balance -= int(withdraw_amount)
        transaction_histroy.append(f"withdrew {withdraw_amount}")
        shown_balance.config(text=f"Your balance is: ${balance}")
        #removing the deposit amount entry and label
        entered_amounts.destroy()  
        amount_label.destroy()  
        submit_button.destroy() 
        label.config(text="withdraw succesful",fg="black")
        #returning the buttons
        deposit_button.grid(row=4, column=0, padx=5, pady=10)
        withdraw_button.grid(row=4, column=1, padx=5, pady=10)
        history_button.grid(row=4, column=2, padx=5, pady=10)
        cancel_button.destroy()
    except ValueError:
        if withdraw_amount > balance:
            label.config(text="insufficient funds",fg="red")
        else:
            label.config(text="Invalid input. Please enter a valid number.")

def cancel(entered_amounts,amount_label,submit_button,cancel_button):
    #removing the deposit amount entry and label
    entered_amounts.grid_forget()  
    amount_label.grid_forget()  
    submit_button.grid_forget() 
    label.config(text="cancelled",fg="black")
    #recreating the buttons
    deposit_button.grid(row=4, column=0, padx=5, pady=10)
    withdraw_button.grid(row=4, column=1, padx=5, pady=10)
    history_button.grid(row=4, column=2, padx=5, pady=10)
    #removing itself
    cancel_button.destroy()


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
#label used for messages
label = Label(root, text=f"",fg="red")
label.grid(row=1, column=0, padx=5, pady=10,columnspan=4,rowspan=2)

#withdraw, deposit labels


#buttons for user actions
#deposit
deposit_button = Button(root, text="Deposit", command=lambda:deposit())
deposit_button.grid(row=4, column=0, padx=5, pady=10)
#withdraw
withdraw_button = Button(root, text="Withdraw", command=lambda:withdraw())
withdraw_button.grid(row=4, column=1, padx=5, pady=10)
#transaction history
history_button = Button(root, text="History", )
history_button.grid(row=4, column=2, padx=5, pady=10)

#button to quit the program
close = Button(root, text="Close", command=root.quit)
close.grid(row=4, column=3, padx=5, pady=10)


#running the main loop
root.mainloop()



