# This is a simple bank account simulator that allows users to create an account, deposit money, withdraw money, and check their balance.

#explain why the code is used

from tkinter import *
import datetime
#import matplotlib

#initial constants
balance = 0
transaction_histroy = []
user_info = {} #{"username": "password"} 
amount = 0
deposit_amount = 0
#time for transaction data
time = datetime.date.today()
time = time.strftime("%a %d %b %Y")



#function for depositing money
def deposit():
    #clrear any labels
    label.config(text="")
    #sets up the label and entry box for the deposits
    #clears the entry box for previous enters
    entered_amounts.delete(0,"end")
    entered_amounts.grid(row=2, column=1, padx=10, pady=10,columnspan=4,)
    #shows label
    amount_label.configure(text="Enter amount to deposit: ")
    amount_label.grid(row=1, column=1, padx=10, pady=10,columnspan=4)
    #submit_button = Button(root, text="Submit", command=lambda: deposit_submit(entered_amounts,amount_label,submit_button,cancel_button))
    submit_button.configure(command=lambda: deposit_submit(entered_amounts,amount_label,submit_button,cancel_button))
    submit_button.grid(row=3, column=2, padx=10, pady=10)
    #adds cancel button
    cancel_button.grid(row=3, column=3, padx=5, pady=10)


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

        #removing entry information
        entered_amounts.grid_forget()  
        amount_label.grid_forget()  
        submit_button.grid_forget()
        label.config(text="deposit succesful",fg="black")

        cancel_button.grid_forget()
    except ValueError:
        label.config(text="Invalid input. Please enter a valid number.",fg="red")


#function for withdrawing money
def withdraw():
    #clrear any labels
    label.config(text="")

    #sets up the label and entry box for the withdraw
    entered_amounts.delete(0,"end")
    entered_amounts.grid(row=2, column=1, padx=10, pady=10,columnspan=4,)

    #adds amount labels
    amount_label.configure(text="Enter amount to withdraw: ")
    amount_label.grid(row=1, column=1, padx=10, pady=10,columnspan=4)

    #adds submit button
    submit_button.configure(command=lambda: withdraw_submit(entered_amounts,amount_label,submit_button,cancel_button))
    submit_button.grid(row=3, column=2, padx=5, pady=10)

    #adds cancel button
    cancel_button.grid(row=3, column=3, padx=5, pady=10)


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

        #removing entry information
        entered_amounts.grid_forget()  
        amount_label.grid_forget()  
        submit_button.grid_forget()
        label.config(text="withdraw succesful",fg="black")

        #removing cancel button
        cancel_button.grid_forget()
    #catching errors
    except ValueError:
        if withdraw_amount > balance:
            label.config(text="insufficient funds",fg="red")
        else:
            label.config(text="Invalid input. Please enter a valid number.", fg="red")

#function for canceling actions such as deposit and withdraw
def cancel(entered_amounts,amount_label,submit_button,cancel_button):
    #removing entry information
    entered_amounts.grid_forget()  
    amount_label.grid_forget()  
    submit_button.grid_forget()
    label.config(text="cancelled",fg="black")

    #removing itself
    cancel_button.grid_forget()


#function to show the transaction history
def user_histroy():    
    history = Tk()
    history.title("Transaction History")
    history.geometry("400x400")

    # Main frame
    main_frame = Frame(history)
    main_frame.pack(fill=BOTH, expand=1)

    # Canvas
    canvas = Canvas(main_frame, bg="blue")
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Scrollbar
    my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    my_scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")
    canvas.configure(yscrollcommand=my_scrollbar.set)

    # Frame inside canvas
    history_frame = Frame(canvas, bg="green")
    canvas.create_window((0, 0), window=history_frame, anchor="nw")

    # Track scrollability
    can_scroll_verticaly = [False]
    can_scroll_horizontaly = [False]

    # Update scrollregion and scrollability flags
    def update_scroll_flags():
        canvas.update_idletasks()
        bbox = canvas.bbox("all")
        if bbox:
            canvas.configure(scrollregion=bbox)
            canvas_width = canvas.winfo_width()
            canvas_height = canvas.winfo_height()
            content_width = bbox[2] - bbox[0]
            content_height = bbox[3] - bbox[1]
            can_scroll_verticaly[0] = content_height > canvas_height
            can_scroll_horizontaly[0] = content_width > canvas_width

    def delayed_update(event=None):
        history.after(50, update_scroll_flags)

    canvas.bind("<Configure>", delayed_update)

    # Mouse wheel events
    def on_mouse_wheel(event):
        if can_scroll_verticaly[0]:
            canvas.yview_scroll(-int(event.delta / 50), "units")

    def on_shift_mouse_wheel(event):
        if can_scroll_horizontaly[0]:
            canvas.xview_scroll(-int(event.delta / 50), "units")

    canvas.bind_all("<MouseWheel>", on_mouse_wheel)
    canvas.bind_all("<Shift-MouseWheel>", on_shift_mouse_wheel)

    # Header
    label = Label(history_frame, text="Transaction History", font=("Arial", 20), bg="red")
    label.pack()

    # Transaction content
    for transaction in transaction_histroy:
        transaction_label = Label(history_frame, text=transaction, font=("Arial", 12), bg="green")
        transaction_label.pack(anchor="w", padx=10, pady=5)


def signup():
    #removing the login and signup buttons
    login_button.grid_forget()
    signup_button.grid_forget()

    login_label.config(text="Create an account")
    age_label = Label(login_screen, text="Age:")
    age_label.grid(row=2, column=1, padx=5, pady=10)
    age = Entry(login_screen)  
    age.grid(row=2, column=2, padx=5, pady=10)
    username_label = Label(login_screen, text="Username:")
    username_label.grid(row=3, column=1, padx=5, pady=10)
    username = Entry(login_screen)
    username.grid(row=3, column=2, padx=5, pady=10)
    password_label = Label(login_screen, text="Password:")
    password_label.grid(row=4, column=1, padx=5, pady=10)
    password = Entry(login_screen)
    password.grid(row=4, column=2, padx=5, pady=10)
    confirm_password_label = Label(login_screen, text="Confirm Password:") 
    confirm_password_label.grid(row=5, column=1, padx=5, pady=10)
    confirm_password = Entry(login_screen)
    confirm_password.grid(row=5, column=2, padx=5, pady=10)
    signup_submit_button = Button(login_screen, text="Submit", command=lambda: signup_submit(username,password,confirm_password,error_label,age), bd=0)
    signup_submit_button.grid(row=6, column=1, padx=5, pady=10,columnspan=2)
    error_label = Label(login_screen, text="", fg="red")
    

def signup_submit(username,password,confirm_password,error_label,age):
    try:
        if username.get().strip(" ") == "" or password.get() == "" or confirm_password.get() == "":
            error_label.grid(row=1, column=1, columnspan=2, padx=5, pady=10)
            error_label.config(text="All fields are required", fg="red")
        elif password.get() != confirm_password.get():
                error_label.grid(row=1, column=1, columnspan=2, padx=5, pady=10)
                error_label.config(text="Passwords do not match", fg="red")
        elif int(age.get()) <13:
            error_label.grid(row=1, column=1, columnspan=2, padx=5, pady=10)
            error_label.config(text="You must be at least 13 years old to create an account", fg="red")
        else:
            #saves the users information in a dictionary
            user_info[username.get()] = password.get()
            print(user_info)
            #removes the signup page
            root.deiconify()
            login_screen.destroy()
            
    except ValueError:
        error_label.grid(row=1, column=1, columnspan=2, padx=5, pady=10)
        error_label.config(text="Invalid age. Please enter a valid number.", fg="red")
        


        
#setting up login signup screen
login_screen = Tk()
login_screen.title("Bank Account login")
login_screen.geometry("800x600")

#centering the items
login_screen.grid_columnconfigure(0, weight=1)
login_screen.grid_columnconfigure(5, weight=1)

#creating a label for the login screen
login_label = Label(login_screen, text="Welcome to the Bank Account Simulator")
login_label.grid(row=0, column=1, padx=5, pady=10, columnspan=4)
login_button = Button(login_screen, text="Login", command=lambda: signup(), bd=0)
login_button.grid(row=1, column=2, padx=5, pady=10)
signup_button = Button(login_screen, text="signup", command=lambda: signup(), bd=0)
signup_button.grid(row=1, column=3, padx=5, pady=10)

#running the login screen
#login_screen.mainloop()

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
#frame for astethics
left_col_frame = Frame(root, bg="lightgray", width=50)
left_col_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")

#deposit button
deposit_button = Button(root, text="Deposit", command=lambda:deposit(),bd=0)
deposit_button.grid(row=1, column=0, padx=5, pady=10)

#withdraw button
withdraw_button = Button(root, text="Withdraw", command=lambda:withdraw(),bd=0)
withdraw_button.grid(row=2, column=0, padx=5, pady=10)

#history button
history_button = Button(root, text="History",command=lambda:user_histroy(), bd=0)
history_button.grid(row=3, column=0, padx=5, pady=10)

#close button
close = Button(root, text="Close", command=root.quit,bd=0)
close.grid(row=4, column=0, padx=5, pady=10)

#entery information
entered_amounts = Entry(root)
amount_label = Label(root, text="Enter amount to deposit: ")
submit_button = Button(root, text="Submit", command=lambda: deposit_submit(entered_amounts,amount_label,submit_button,cancel_button))
cancel_button = Button(root, text="Cancel", command=lambda:cancel(entered_amounts,amount_label,submit_button,cancel_button))

#running the main loop, will run after the login screen is closed
#root.mainloop()
root.withdraw()  

#running the login screen
login_screen.mainloop()
