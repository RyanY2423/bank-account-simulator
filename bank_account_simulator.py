# This is a simple bank account simulator that allows users to create an account, deposit money, withdraw money, and check their balance.

#explain why the code is used

from tkinter import *
import datetime
import os
import json

#making sure the current directory is the same as the file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#initial constants
#initial information of the user
balance = 0
transaction_history = []
user_password = ""
user_username = ""
#where the user information is stored in the file used for writing into the file at the end
user_info_location = 0
#amount user deposits/withdraws
amount = 0

#time for transaction data
time = datetime.date.today()
time = time.strftime("%a %d %b %Y")

#Functions used for signing up and logging in
#function for signing up page
def signup():
    #removing the login and signup buttons
    login_button.grid_forget()
    signup_button.grid_forget()
    #creating label for login
    login_label.config(text="Create an account")

    #creating the label and entry for age
    age_label.grid(row=2, column=1, padx=5, pady=10)
    age.grid(row=2, column=2, padx=5, pady=10)

    #creating the label and entry for username
    username_label.grid(row=3, column=1, padx=5, pady=10)
    username.delete(0,END)
    username.grid(row=3, column=2, padx=5, pady=10)

    #creating the label and entry for password
    password_label.grid(row=4, column=1, padx=5, pady=10)
    password.delete(0,END)
    password.grid(row=4, column=2, padx=5, pady=10)

    #creating the label and entry for confirm password
    confirm_password_label.grid(row=5, column=1, padx=5, pady=10)
    confirm_password.grid(row=5, column=2, padx=5, pady=10)
    
    #creating the label and entry for signup button
    signup_submit_button.grid(row=6, column=2, padx=5, pady=10)
    #creating the cancel button
    cancel_button.grid(row=6, column=1, padx=5, pady=10)
    
    
#function for submit button when signing up
def signup_submit(username,password,confirm_password,age):
    #globals location of the user information in the file
    global user_info_location
    try:      
        #checking if all the fields have been filled
        if username.get().strip(" ") == "" or password.get() == "" or confirm_password.get() == "":
            error_label.grid(row=1, column=1, columnspan=2, padx=5, pady=10)
            error_label.config(text="All fields are required", fg="red")
        #checks if the password and confirmed password is the same
        elif password.get() != confirm_password.get():
                error_label.grid(row=1, column=1, columnspan=2, padx=5, pady=10)
                #tells the users the passwords are not the same
                error_label.config(text="Passwords do not match", fg="red")
        #checking if their age is over 13
        elif int(age.get()) <13:
            error_label.grid(row=1, column=1, columnspan=2, padx=5, pady=10)
            error_label.config(text="You must be at least 13 years old to create an account", fg="red")
        #checking if their age is under 100
        elif int(age.get()) >100:
            error_label.grid(row=1, column=1, columnspan=2, padx=5, pady=10)
            error_label.config(text="enter a valid age", fg="red")
        else:
            #opens file with user data
            with open("user_account_info.json", "r") as file:
                users_information = json.load(file)
                #check if the username is in the file
                for does_user_exist in users_information:
                    #if user is in file show message
                    if does_user_exist["username"] == username.get():
                        error_label.grid(row=1, column=1, columnspan=2, padx=5, pady=10)
                        error_label.config(text="account already exists", fg="red")
                        file.close
                        #ending the function to not run the adding new account to file
                        return
                file.close
                #getting user data
                user_username = username.get()
                user_password = password.get()
                #saving user location in the file
                user_info_location = -1
                #writes new user data to external file
                with open("user_account_info.json","w") as file:
                    users_information.append({'username': user_username, 'password': user_password, 'balance': balance, 'transaction_history': transaction_history})
                    json.dump(users_information,file,indent=2)

            #removes the signup page and starts main 
            login_screen.destroy()  
            main_program()
    #catching errors              
    except ValueError:
        error_label.grid(row=1, column=1, columnspan=2, padx=5, pady=10)
        error_label.config(text="Invalid age. Please enter a valid number.", fg="red")
    #function for login
def login():
    #removes the login and signup buttons
    login_button.grid_forget()
    signup_button.grid_forget()
#changes the login label to show that the user is logging in
    login_label.config(text="log into your account")
    #creating the label and entry for username
    username_label.grid(row=2, column=1, padx=5, pady=5)
    username.delete(0,END)
    username.grid(row=2, column=2, padx=5, pady=5)
    #creating the label and entry for password
    password_label.grid(row=3, column=1, padx=5, pady=5)
    password.delete(0,END)
    password.grid(row=3, column=2, padx=5, pady=5)  
    #creating the submit button
    login_submit_button.grid(row=6, column=2, padx=5, pady=10)
    #creating the cancel button
    cancel_button.grid(row=6, column=1, padx=5, pady=10)
    
#function for submit button when logging in
def login_submit(username,password):
    #globals balance transaction_history and user_info_location for main program use
    global balance
    global transaction_history
    global user_info_location
    #gathering the users information fro mthe eternal file
    with open("user_account_info.json", "r") as file:
        users_information = json.load(file)
        for does_user_exist in users_information:    
            #cehcks if the user exists       
            if does_user_exist["username"] == username.get():    
                #gathers the required information  
                user_password = does_user_exist["password"]
                balance = float(does_user_exist["balance"])
                transaction_history = does_user_exist["transaction_history"]
                #checks if the user entered the correct password
                if user_password != password.get():
                    error_label.grid(row=1, column=1, columnspan=2, padx=5, pady=10)
                    error_label.config(text="incorrect password", fg="red")
                    #stop the function to not run the new account code
                    return
                else: 
                    #saves the position of the user in the file
                    #this is used to write the user data back to the file at the end of the program
                    user_info_location = users_information.index({'username': username.get(), 'password': password.get(),    
                                                                      'balance': balance, 'transaction_history': transaction_history})
                    login_screen.destroy()  # Destroys the login screen
                    main_program() # Call the main program function	
                    #stop the function to not run the new account code
                    return
        #creates the bew account button if the account inputted does not exist
        new_account.grid(row=1, column=1, columnspan=2, pady=10)    
    #close the file           
    file.close()

#function to cancel the login and signup process, returns to the login screen
def login_signup_cancel():
    #puts the log in and signup buttons back into the program
    login_label.config(text="Welcome to the Bank Account Simulator")
    login_button.grid(row=1, column=2, padx=5, pady=5)
    signup_button.grid(row=1, column=3, padx=5, pady=5)
    #forgets all the labels and entry for login and signup, every label and entry are added to make sure the page only has the necessary information
    age_label.grid_forget()
    age.grid_forget()
    username_label.grid_forget()
    username.grid_forget()
    password_label.grid_forget()
    password.grid_forget()
    confirm_password_label.grid_forget()
    confirm_password.grid_forget()
    signup_submit_button.grid_forget()
    username_label.grid_forget()
    username.grid_forget()
    password_label.grid_forget()
    password.grid_forget()
    login_submit_button.grid_forget()
    cancel_button.grid_forget()
    error_label.grid_forget()
    new_account.grid_forget()

#function for new account creation from login screen, goes from login to signup
def new_acc():
    login_signup_cancel()
    signup()
 
#Functions for the main prgram
def main_program():
    #function for depositing money
    def deposit():
        #clrear any labels
        label.config(text="")
        #sets up the label and entry box for the deposits
        #clears the entry box for previous enters
        entered_amounts.delete(0,"end")
        entered_amounts.grid(row=2, column=1, padx=10, pady=10,columnspan=4,)
        #shows and configure label for deposit
        amount_label.configure(text="Enter amount to deposit: ")
        amount_label.grid(row=1, column=1, padx=10, pady=10,columnspan=4)
        #shows and configures the submit button to deposit
        submit_button.configure(command=lambda: deposit_submit(entered_amounts,amount_label,submit_button,cancel_button))
        submit_button.grid(row=3, column=2, padx=10, pady=10)
        #adds cancel button
        cancel_button.grid(row=3, column=3, padx=5, pady=10)


    #function to submit deposit 
    def deposit_submit(entered_amounts,amount_label,submit_button,cancel_button):
        global balance
        try:
            #checks if the deposit amount is a number
            deposit_amount = round(float(entered_amounts.get()),2)
            if deposit_amount < 0:
                #if the amount is negative it will give an error
                raise ValueError
            balance += float(deposit_amount)
            #adds deposit to transaction history
            transaction_history.append(f"{time} - Deposited {deposit_amount} ")
            #updates the balance
            shown_balance.config(text=f"Your balance is: ${balance}")

            #removing entry information
            entered_amounts.grid_forget()  
            amount_label.grid_forget()  
            submit_button.grid_forget()
            cancel_button.grid_forget()
            label.config(text="deposit succesful",fg="black")
        
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
        #sets the withraw to 0
        withdraw_amount = 0
        #to catch errors
        try:
            #withdraw amount
            withdraw_amount = round(float(entered_amounts.get()),2)
            if withdraw_amount < 0:
                #if the amount is negative it will give an error
                raise ValueError
            elif withdraw_amount > balance:
                #if the amount is more than the balance it will give an error
                raise ValueError
            balance -= float(withdraw_amount)
            #adds withdraw to transaction history
            transaction_history.append(f"{time} - withdrew {withdraw_amount}")
            #updates the balance
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
    def user_history():    
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

        # Frame in which the contents go into
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
        #moving the canvas
        canvas.bind("<Configure>", delayed_update)

        # Mouse wheel events
        def on_mouse_wheel(event):
            if can_scroll_verticaly[0]:
                canvas.yview_scroll(-int(event.delta / 50), "units")
        #when crolling sideways with mouse when holding shift
        def on_shift_mouse_wheel(event):
            if can_scroll_horizontaly[0]:
                canvas.xview_scroll(-int(event.delta / 50), "units")
        #moving the canvas
        canvas.bind_all("<MouseWheel>", on_mouse_wheel)
        canvas.bind_all("<Shift-MouseWheel>", on_shift_mouse_wheel)

        # Header
        label = Label(history_frame, text="Transaction History", font=("Arial", 20), bg="red")
        label.pack()

        # Transaction content
        for transaction in transaction_history:
            transaction_label = Label(history_frame, text=transaction, font=("Arial", 12), bg="green")
            transaction_label.pack(anchor="w", padx=10, pady=5)

    #function to close the program and save user data to file
    def close_program():
        with open("user_account_info.json", "r") as file:
            #getting the user information
            users_information = json.load(file)                      
            file.close
        #updating user information file
        users_information[user_info_location]["balance"] = balance
        users_information[user_info_location]["transaction_history"] = transaction_history
        with open("user_account_info.json", "w") as file:
            json.dump(users_information, file, indent=2)
        root.destroy()

    
    


    #main program
    #creating a window
    root = Tk()
    root.title("Bank Account Simulator")
    root.geometry("800x600")
    #colour of the background
    root.config(background="#252526")

    #centering the items
    root.grid_columnconfigure(0, weight=0)
    root.grid_columnconfigure(5, weight=1)

    #creating a fram for the main information for deposit and withdraw functions
    main_frame = Frame(root)
    main_frame.grid(row=0, column=1, columnspan=4)

    #creating labels for the main page
    shown_balance = Label(main_frame, text=f"your balance is: ${balance}",font=("Arial",20))
    shown_balance.grid(row=0, column=1, padx=5, pady=5,columnspan=4)
    #label used for messages
    label = Label(main_frame, text=f"")#,width=40
    label.grid(row=1, column=0, padx=5, pady=10,columnspan=4,rowspan=2)

    #entery information
    entered_amounts = Entry(main_frame)
    amount_label = Label(main_frame, text="Enter amount to deposit: ")
    submit_button = Button(main_frame, text="Submit", command=lambda: deposit_submit(entered_amounts,amount_label,submit_button,cancel_button))
    cancel_button = Button(main_frame, text="Cancel", command=lambda:cancel(entered_amounts,amount_label,submit_button,cancel_button))

    #buttons for user actions
    #frame for astethics
    left_col_frame = Frame(root, bg="#131314", width=70,height=600)
    left_col_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")
    left_col_frame.grid_propagate(False)
    spacer = Label(left_col_frame, text="", bg="#131314")
    spacer.grid(row=0, column=0, pady=10)
    #deposit button
    deposit_button = Button(left_col_frame, text="Deposit", command=lambda:deposit(),bd=0)
    deposit_button.grid(row=1, column=0, padx=5,pady=5, sticky="n")

    #withdraw button
    withdraw_button = Button(left_col_frame, text="Withdraw", command=lambda:withdraw(),bd=0)
    withdraw_button.grid(row=2, column=0, padx=5,pady=5,sticky="n")

    #history button
    history_button = Button(left_col_frame, text="History",command=lambda:user_history(), bd=0)
    history_button.grid(row=3, column=0, padx=5,pady=5,sticky="n")

    #close button
    close = Button(left_col_frame, text="Close", command=close_program,bd=0)
    close.grid(row=4, column=0, padx=5,pady=5,sticky="n")

    #checks when the program is closed via the x and runs the close window function to save user data
    root.protocol("WM_DELETE_WINDOW", close_program)  
    root.mainloop()  # Start the main loop of the program
    

    

    #running the main loop, will run after the login screen is closed


#setting up login signup screen
login_screen = Tk()
login_screen.title("Bank Account login")
login_screen.geometry("800x600")
login_screen.config(bg="#252526")

#centering the items
login_screen.grid_columnconfigure(0, weight=1)
login_screen.grid_columnconfigure(5, weight=1)

#creating a label for the login screen
login_label = Label(login_screen, text="Welcome to the Bank Account Simulator",bg="#252526",fg="#e7efef")
login_label.grid(row=0, column=1, padx=5, pady=5, columnspan=4)
login_button = Button(login_screen, text="Login", command=lambda: login(), bd=0,bg="#252526",fg="#e7efef")
login_button.grid(row=1, column=2, padx=5, pady=5)
signup_button = Button(login_screen, text="signup", command=lambda: signup(), bd=0,bg="#252526",fg="#e7efef")
signup_button.grid(row=1, column=3, padx=5, pady=5)
cancel_button = Button(login_screen, text="Cancel", bd=0,command=lambda:login_signup_cancel(),bg="#252526",fg="#e7efef")
#creating error label which will be used if an error occurs
error_label = Label(login_screen, text="", fg="red",bg="#252526")

#creating labels for the sign up button
age_label = Label(login_screen, text="Age:",bg="#252526",fg="#e7efef")
age = Entry(login_screen)  
username_label = Label(login_screen, text="Username:",bg="#252526",fg="#e7efef")
username = Entry(login_screen)
password_label = Label(login_screen, text="Password:",bg="#252526",fg="#e7efef")
password = Entry(login_screen,show="*")
confirm_password_label = Label(login_screen, text="Confirm Password:",bg="#252526",fg="#e7efef") 
confirm_password = Entry(login_screen,show="*")#show="*" used to hide the password user enters
signup_submit_button = Button(login_screen, text="Submit", command=lambda: signup_submit(username,password,confirm_password,age), bd=0,bg="#252526",fg="#e7efef")


#creating labels for the log in button
username_label = Label(login_screen, text="Username:",bg="#252526",fg="#e7efef")
username = Entry(login_screen)
password_label = Label(login_screen, text="Password:",bg="#252526",fg="#e7efef")
password = Entry(login_screen,show="*")
login_submit_button = Button(login_screen, text="Submit", command=lambda: login_submit(username,password), bd=0,bg="#252526",fg="#e7efef",activebackground="#252526")
#button for creating a new account if login fails for account not existing
new_account = Button(login_screen,text="user does not exist, create new account?", command=lambda:new_acc(),bd=0,fg="red",bg="#252526",)
#running the login screen
login_screen.mainloop()




