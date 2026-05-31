from tkinter import *

def navbar(outerFrame,root):

    def openCart():
        from shoppingCart import shoppingCart
        outerFrame.destroy()
        shoppingCart(root)

    def openOrders():
        from ordersScreen import ordersScreen
        outerFrame.destroy()
        ordersScreen(root)

    def openAdmin():
        from adminDashboardScreen import adminDashboardScreen
        outerFrame.destroy()
        adminDashboardScreen(root);


    def logoutAction():
        from loginScreen import loginScreen
        outerFrame.destroy()
        loginScreen(root)

    def gotoHome():
        from homeScreen import homeScreen
        outerFrame.destroy()
        homeScreen(root)


    # NAVBAR
    navbarFrame = Frame(outerFrame,bg="#D9D9D9",height=60)

    navbarFrame.pack(fill="x")
    navbarFrame.pack_propagate(False)


	# NAV BUTTONS FRAME
    navButtonsFrame = Frame(
        navbarFrame,
        bg="#D9D9D9"
    )

    navButtonsFrame.pack(
        side="right",
        padx=20
    )

	# CART BUTTON
    cartBtn = Button(
        navButtonsFrame,
        text="Cart",
        font=("Arimo", 10, "bold"),
        bg="#1C4975",
        fg="white",
        bd=0,
        padx=10,
        pady=5,
        cursor="hand2",
        command=openCart
    )

    cartBtn.pack(
        side="left",
        padx=5
    )

	# ORDERS BUTTON
    ordersBtn = Button(
        navButtonsFrame,
        text="Orders",
        font=("Arimo", 10, "bold"),
        bg="#1C4975",
        fg="white",
        bd=0,
        padx=10,
        pady=5,
        cursor="hand2",
        command=openOrders
    )

    ordersBtn.pack(
        side="left",
        padx=5
    )

	# ADMIN BUTTON
    adminBtn = Button(
        navButtonsFrame,
        text="Admin",
        font=("Arimo", 10, "bold"),
        bg="#B22222",
        fg="white",
        bd=0,
        padx=10,
        pady=5,
        cursor="hand2",
        command=openAdmin
    )

    adminBtn.pack(
        side="left",
        padx=5
    )

	# LOGOUT BUTTON
    logoutBtn = Button(
        navButtonsFrame,
        text="Logout",
        font=("Arimo", 10, "bold"),
        bg="#555555",
        fg="white",
        bd=0,
        padx=10,
        pady=5,
        cursor="hand2",
        command=logoutAction
    )

    logoutBtn.pack(
        side="left",
        padx=5
    )

    StoreTitle=Label(navbarFrame,text="OnlySocks",font=("Arimo", 22, "bold"),bg="#D9D9D9",fg="#1C4975")
    StoreTitle.pack(side=LEFT,padx=20)
    StoreTitle.bind( "<Button-1>", lambda e:gotoHome() )
