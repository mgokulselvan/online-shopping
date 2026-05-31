from tkinter import *
from navbar import navbar

def adminDashboardScreen(root):

    adminFrame = Frame(
        root,
        bg="#E6E6E6"
    )

    adminFrame.pack(
        fill="both",
        expand=True
    )


    def openInventoryManagement():
        from inventoryScreen import inventoryScreen
        adminFrame.destroy()
        inventoryScreen(root)

    def openOrdersManagement():
        from adminOrdersScreen import adminOrdersScreen
        adminFrame.destroy()
        adminOrdersScreen(root)


    navbar(adminFrame,root)

    # =========================
    # TITLE SECTION
    # =========================

    titleFrame = Frame(
        adminFrame,
        bg="#E6E6E6"
    )

    titleFrame.pack(
        fill="x",
        padx=30,
        pady=(25,15)
    )

    adminTitle = Label(
        titleFrame,
        text="Admin Dashboard",
        font=("Arimo", 30, "bold"),
        bg="#E6E6E6",
        fg="#1B1C1C"
    )

    adminTitle.pack(anchor="w")

    subtitleLabel = Label(
        titleFrame,
        text="Manage products and customer orders",
        font=("Arimo", 11),
        bg="#E6E6E6",
        fg="#6E6E6E"
    )

    subtitleLabel.pack(
        anchor="w",
        pady=(4,0)
    )

    divider = Frame(
        titleFrame,
        bg="#B0B0B0",
        height=1
    )

    divider.pack(
        fill="x",
        pady=(15,0)
    )

    # =========================
    # BUTTON SECTION
    # =========================

    buttonContainer = Frame(
        adminFrame,
        bg="#E6E6E6"
    )

    buttonContainer.pack(
        expand=True
    )

    # INVENTORY BUTTON

    inventoryBtn = Button(
        buttonContainer,
        text="Inventory Management",
        font=("Arimo", 16, "bold"),
        bg="#1C4975",
        fg="white",
        width=25,
        height=2,
        bd=0,
        cursor="hand2",
        command=openInventoryManagement
    )

    inventoryBtn.pack(
        pady=15
    )

    # ORDERS BUTTON

    ordersBtn = Button(
        buttonContainer,
        text="Orders Management",
        font=("Arimo", 16, "bold"),
        bg="#B22222",
        fg="white",
        width=25,
        height=2,
        bd=0,
        cursor="hand2",
        command=openOrdersManagement
    )

    ordersBtn.pack(
        pady=15
    )
