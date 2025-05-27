# This is a simple bank account simulator that allows users to create an account, deposit money, withdraw money, and check their balance.

#explain why the code is used

from tkinter import *
import datetime
#import matplotlib

#initial balance, set at 0 as there is no accounts yet
balance = 0
transaction_histroy = ["test","test","test","test","test","test","test","test","test","test","test","test","test","test","test","test","test","test","test","test","test","test","test","test"]
amount = 0
deposit_amount = 0
time = datetime.date.today()
time = time.strftime("%a %d %b %Y")



#function for depositing money
def deposit():
    #clrear any labels
    label.config(text="")
    #deletes inputs for withdraw to prevent overlapping	
    deposit_button.grid_forget()
    withdraw_button.grid_forget()
    history_button.grid_forget()
    cancel_button = Button(root, text="Cancel", command=lambda:cancel(entered_amounts,amount_label,submit_button,cancel_button))
    cancel_button.grid(row=3, column=1, padx=5, pady=10)
    #sets up the label and entry box for the deposits
    entered_amounts = Entry()
    entered_amounts.grid(row=2, column=1, padx=10, pady=10,columnspan=4,)
    amount_label = Label(root, text="Enter amount to deposit: ")
    amount_label.grid(row=1, column=1, padx=10, pady=10,columnspan=4)
    submit_button = Button(root, text="Submit", command=lambda: deposit_submit(entered_amounts,amount_label,submit_button,cancel_button))
    submit_button.grid(row=3, column=2, padx=10, pady=10)



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
        transaction_histroy.append(f"{time} - Deposited {deposit_amount} ")
        shown_balance.config(text=f"Your balance is: ${balance}")
        #removing the deposit amount entry and label
        entered_amounts.destroy()  
        amount_label.destroy()  
        submit_button.destroy() 
        label.config(text="deposit succesful",fg="black")
        #returning the buttons
        deposit_button.grid(row=3, column=1, padx=5, pady=10)
        withdraw_button.grid(row=3, column=2, padx=5, pady=10)
        history_button.grid(row=3, column=3, padx=5, pady=10)
        cancel_button.destroy()
    except ValueError:
        label.config(text="Invalid input. Please enter a valid number.",fg="red")


#function for withdrawing money
def withdraw():
    #clrear any labels
    label.config(text="")
    #deletes inputs for deposit to prevent overlapping
    deposit_button.grid_forget()
    withdraw_button.grid_forget()
    history_button.grid_forget()
    #sets up the label and entry box for the withdraw
    entered_amounts = Entry()
    entered_amounts.grid(row=2, column=1, padx=10, pady=10,columnspan=4,)
    amount_label = Label(root, text="Enter amount to withdraw: ")
    amount_label.grid(row=1, column=1, padx=10, pady=10,columnspan=4)
    submit_button = Button(root, text="Submit", command=lambda: withdraw_submit(entered_amounts,amount_label,submit_button,cancel_button))
    submit_button.grid(row=3, column=2, padx=10, pady=10)
    cancel_button = Button(root, text="Cancel", command=lambda:cancel(entered_amounts,amount_label,submit_button,cancel_button))
    cancel_button.grid(row=3, column=1, padx=5, pady=10)


#function to submiot withdraw
def withdraw_submit(entered_amounts,amount_label,submit_button,cancel_button):
    global balance
    withdraw_amount = 0
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
        transaction_histroy.append(f"{time} - withdrew {withdraw_amount}")
        shown_balance.config(text=f"Your balance is: ${balance}")
        #removing the deposit amount entry and label
        entered_amounts.destroy()  
        amount_label.destroy()  
        submit_button.destroy() 
        label.config(text="withdraw succesful",fg="black")
        #returning the buttons
        deposit_button.grid(row=3, column=1, padx=5, pady=10)
        withdraw_button.grid(row=3, column=2, padx=5, pady=10)
        history_button.grid(row=3, column=3, padx=5, pady=10)
        cancel_button.destroy()
    except ValueError:
        if withdraw_amount > balance:
            label.config(text="insufficient funds",fg="red")
        else:
            label.config(text="Invalid input. Please enter a valid number.", fg="red")

#function for canceling actions such as deposit and withdraw
def cancel(entered_amounts,amount_label,submit_button,cancel_button):
    #removing the deposit amount entry and label
    entered_amounts.destroy()  
    amount_label.destroy()  
    submit_button.destroy() 
    label.config(text="cancelled",fg="black")
    #recreating the buttons
    deposit_button.grid(row=3, column=1, padx=5, pady=10)
    withdraw_button.grid(row=3, column=2, padx=5, pady=10)
    history_button.grid(row=3, column=3, padx=5, pady=10)
    #removing itself
    cancel_button.destroy()




#function to show the transaction history
def user_histroy():    
    history = Tk()
    history.title("Transaction History")
    history.geometry("400x400")

#making the main frame to put the canvas
    main_frame = Frame(history)
    main_frame.pack(fill=BOTH, expand=1)

#creating the canvas
    canvas = Canvas(main_frame, bg="blue")
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

#letting the scrollbar be scrolled with a mouse 
    canvas.bind_all('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta / 50), "units"))
    
#makling the scrollbar
    my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

#moving the scorllbar
    canvas.configure(yscrollcommand=my_scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    #creating a frame for the history
    history_frame = Frame(canvas,bg="green")
    canvas.create_window((0, 0), window=history_frame, anchor="nw")

    label = Label(history_frame, text="Transaction History", font=("Arial", 20),background=None)
    label.pack()
#shows all transactions
    for transaction in transaction_histroy:
        transaction = Label(history_frame, text=transaction, font=("Arial", 12),bg="green")
        transaction.pack(anchor="w", padx=10, pady=5)
    history.mainloop()
        
        


#main program
#creating a window
root = Tk()
root.title("Bank Account Simulator")
root.geometry("800x600")
#colour of the background, currently set at hideous blue
#root.config(background="blue")

#centering the items
root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(5, weight=1)



#creating labels for the main page
shown_balance = Label(root, text=f"your balance is: ${balance}",font=("Arial",20))
shown_balance.grid(row=0, column=1, padx=5, pady=5,columnspan=4)
#label used for messages
label = Label(root, text=f"")#,width=40
label.grid(row=1, column=1, padx=5, pady=10,columnspan=4,rowspan=2)



#buttons for user actions
#deposit
deposit_button = Button(root, text="Deposit", command=lambda:deposit())
deposit_button.grid(row=3, column=1, padx=5, pady=10)
#withdraw
withdraw_button = Button(root, text="Withdraw", command=lambda:withdraw())
withdraw_button.grid(row=3, column=2, padx=5, pady=10)
#transaction history
history_button = Button(root, text="History",command=lambda:user_histroy() )
history_button.grid(row=3, column=3, padx=5, pady=10)

#button to quit the program
close = Button(root, text="Close", command=root.quit)
close.grid(row=3, column=4, padx=5, pady=10)


#this is for testing purposes
left_col_frame = Frame(root, bg="lightgray", width=50)
left_col_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")

deposit_button = Button(root, text="Deposit", command=lambda:deposit(),bd=0)
deposit_button.grid(row=1, column=0, padx=5, pady=10)

withdraw_button = Button(root, text="Withdraw", command=lambda:withdraw(),bd=0)
withdraw_button.grid(row=2, column=0, padx=5, pady=10)

history_button = Button(root, text="History",command=lambda:user_histroy(), bd=0)
history_button.grid(row=3, column=0, padx=5, pady=10)

close = Button(root, text="Close", command=root.quit,bd=0)
close.grid(row=4, column=0, padx=5, pady=10)



button = Button(root, text="Button with No Background", highlightthickness=0, bd=0, relief="flat")
button.grid
#running the main loop
root.mainloop()



