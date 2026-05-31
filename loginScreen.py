from tkinter import *

def loginScreen(root):
    main_frame = Frame(root)
    main_frame.pack(expand=True,fill="both")
    main_frame["bg"]="#E6E6E6"

    def openRegister():
        from registerScreen import registerScreen
        main_frame.destroy()
        registerScreen(root)

# NAVBAR
    navbarFrame = Frame(main_frame, bg="#D9D9D9", height=60)

    navbarFrame.pack(fill="x")

    navbarFrame.pack_propagate(False)

    StoreTitle = Label(
        navbarFrame,
        text="OnlySocks",
        font=("Arimo", 22, "bold"),
        bg="#D9D9D9",
        fg="#1C4975"
    )

    StoreTitle.pack(side="left", padx=20)

# TITLE SECTION
    titleFrame = Frame(
        main_frame,
        bg="#E6E6E6"
    )

    titleFrame.pack(
        fill="x",
        padx=20,
        pady=(20, 10)
    )

    registerTitle = Label(
        titleFrame,
        text="Login",
        font=("Arimo", 28, "bold"),
        fg="#1B1C1C",
        bg="#E6E6E6"
    )

    registerTitle.pack(
        anchor="w"
    )

    subtitleLabel = Label(
        titleFrame,
        text="Welcome back to OnlySocks",
        font=("Arimo", 11),
        fg="#6E6E6E",
        bg="#E6E6E6"
    )

    subtitleLabel.pack(
        anchor="w",
        pady=(2, 0)
    )

    divider = Frame(
        titleFrame,
        bg="#B0B0B0",
        height=1
    )

    divider.pack(
        fill="x",
        pady=(12, 0)
    )

# FORM FRAME
    formFrame = Frame(main_frame, bg="#E6E6E6")
    formFrame.pack(pady=10)

    formFrame.columnconfigure(0, weight=1)
    formFrame.columnconfigure(1, weight=1)

# USERNAME
    usernameLabel = Label(formFrame, text="Username:", fg="#1B1C1C", bg="#E6E6E6")
    usernameLabel.grid(row=4, column=0, sticky="w", padx=10, pady=5)

    username = Entry(formFrame, width=30)
    username.grid(row=4, column=1, sticky="ew", padx=10, pady=5)

# PASSWORD
    passLabel = Label(formFrame, text="Set Password:", fg="#1B1C1C", bg="#E6E6E6")
    passLabel.grid(row=5, column=0, sticky="w", padx=10, pady=5)

    password = Entry(formFrame, width=30, show="•")
    password.grid(row=5, column=1, sticky="ew", padx=10, pady=5)


#Show password 
    Checkbutton1=IntVar()

    def tglPsswdVis():
        if Checkbutton1.get() ==1:
            password.config(show="")
        else:
            password.config(show="•")

    ShowBtn=Checkbutton(formFrame,text = "Show Password",variable = Checkbutton1,onvalue=1,offvalue=0,height=2,fg="#1B1C1C",bg="#E6E6E6",command=tglPsswdVis,highlightthickness=0,bd=0)
    ShowBtn.grid(column=0,row=6,sticky="w",padx=5)

#LOGIN
    login_Frame = Frame(main_frame,bd=1)
    login_Frame.pack(padx=2,pady=2,expand=True)
    login_Frame["bg"]="#E6E6E6"

# BOTTOM BAR
    btmBar = Frame(main_frame, bg="#E6E6E6")
    btmBar.pack(side="bottom", fill="x", padx=10, pady=10)

    btmBar.columnconfigure(0, weight=1)
    btmBar.columnconfigure(1, weight=1)

# CREATE ACCOUNT BUTTON
    registerBtn = Button(
        btmBar,
        text="Create Account",
        fg="#1C4975",
        bg="#E6E6E6",
        bd=0,
        highlightthickness=0,
        activebackground="#E6E6E6",
        cursor="hand2",
        command=openRegister
    )

    registerBtn.grid(row=0, column=0, sticky="w")

# LOGIN BUTTON
    loginBtn = Button(
        btmBar,
        text="Login",
        bg="#1C4975",
        fg="#FFFFFF"
    )

    loginBtn.grid(row=0, column=1, sticky="e")
