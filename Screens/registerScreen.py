from tkinter import *

def registerScreen(root):
    main_frame = Frame(root)
    main_frame.pack(expand=True,fill="both")

    main_frame["bg"]="#E6E6E6"

    def openLogin():
        from .loginScreen import loginScreen
        main_frame.destroy()
        loginScreen(root)

    #Register lgoic
    def register():
        from services.register_user import register_user
        if password.get()!=repassword.get():
            messageLabel.config(
                text="Passwords do not match",
                fg="red"
            )
            return

        success = register_user(
            name.get(),
            email.get(),
            phone.get(),
            password.get(),
            address.get()
        )

        if success:
            messageLabel.config(
                text="Registration successful",
                fg="green"
            )
        else:
            messageLabel.config(
                text="Email already exists",
                fg="red"
            )


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
        text="Register",
        font=("Arimo", 28, "bold"),
        fg="#1B1C1C",
        bg="#E6E6E6"
    )

    registerTitle.pack(
        anchor="w"
    )

    subtitleLabel = Label(
        titleFrame,
        text="Create your OnlySocks account",
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

# NAME
    nameLabel = Label(formFrame, text="Name:", fg="#1B1C1C", bg="#E6E6E6")
    nameLabel.grid(row=0, column=0, sticky="w", padx=10, pady=5)

    name = Entry(formFrame, width=30)
    name.grid(row=0, column=1, sticky="ew", padx=10, pady=5)

# EMAIL
    emailLabel = Label(formFrame, text="Email:", fg="#1B1C1C", bg="#E6E6E6")
    emailLabel.grid(row=1, column=0, sticky="w", padx=10, pady=5)

    email = Entry(formFrame, width=30)
    email.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

# PHONE
    phoneLabel = Label(formFrame, text="Phone:", fg="#1B1C1C", bg="#E6E6E6")
    phoneLabel.grid(row=2, column=0, sticky="w", padx=10, pady=5)

    phone = Entry(formFrame, width=30)
    phone.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

# ADDRESS
    addressLabel = Label(formFrame, text="Address:", fg="#1B1C1C", bg="#E6E6E6")
    addressLabel.grid(row=3, column=0, sticky="w", padx=10, pady=5)

    address = Entry(formFrame, width=30)
    address.grid(row=3, column=1, sticky="ew", padx=10, pady=5)

# PASSWORD
    passLabel = Label(formFrame, text="Set Password:", fg="#1B1C1C", bg="#E6E6E6")
    passLabel.grid(row=4, column=0, sticky="w", padx=10, pady=5)

    password = Entry(formFrame, width=30, show="•")
    password.grid(row=4, column=1, sticky="ew", padx=10, pady=5)

# REPASSWORD
    repassLabel = Label(formFrame, text="Reenter Password:", fg="#1B1C1C", bg="#E6E6E6")
    repassLabel.grid(row=5, column=0, sticky="w", padx=10, pady=5)

    repassword = Entry(formFrame, width=30, show="•")
    repassword.grid(row=5, column=1, sticky="ew", padx=10, pady=5)

    #Show password 
    Checkbutton1=IntVar()

    def tglPsswdVis():
        if Checkbutton1.get() ==1:
            password.config(show="")
            repassword.config(show="")
        else:
            password.config(show="•")
            repassword.config(show="•")

# SHOW PASSWORD
    ShowBtn=Checkbutton(formFrame,text = "Show Password",variable = Checkbutton1,onvalue=1,offvalue=0,height=2,fg="#1B1C1C",bg="#E6E6E6",command=tglPsswdVis,highlightthickness=0,bd=0)
    ShowBtn.grid(row=6, column=0, sticky="w", padx=5, pady=5)

#To show the status of registration
    messageLabel = Label(
        formFrame,
        text="",
        fg="red",
        bg="#E6E6E6"
    )

    messageLabel.grid(
        row=6,
        column=0,
        columnspan=2
    )

# BOTTOM BAR
    btmBar = Frame(main_frame, bg="#E6E6E6")
    btmBar.pack(side="bottom", fill="x", padx=10, pady=10)

    btmBar.columnconfigure(0, weight=1)
    btmBar.columnconfigure(1, weight=1)

# Login BUTTON
    loginBtn = Button(
        btmBar,
        text="Login",
        fg="#1C4975",
        bg="#E6E6E6",
        bd=0,
        highlightthickness=0,
        activebackground="#E6E6E6",
        cursor="hand2",
        command=openLogin
    )

    loginBtn.grid(row=0, column=0, sticky="w")

# REGISTER BUTTON
    registerBtn = Button(
        btmBar,
        text="Register",
        bg="#1C4975",
        fg="#FFFFFF",
        command=register
    )

    registerBtn.grid(row=0, column=1, sticky="e")
