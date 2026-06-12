from tkinter import *
from Components import navbar

def adminAddProductScreen(root):

    def addProduct():
        from services.add_product import add_product
        add_product(
                nameEntry.get(),
                categoryEntry.get(),
                priceEntry.get(),
                stockEntry.get(),
                )
        addProductsFrame.destroy()

        from .adminInventoryManagementScreen import (
            adminInventoryManagementScreen
        )

        adminInventoryManagementScreen(root)

    addProductsFrame = Frame(
        root,
        bg="#E6E6E6"
    )

    addProductsFrame.pack(
        fill="both",
        expand=True
    )

    navbar(addProductsFrame,root)
    # =========================
    # TITLE SECTION
    # =========================

    titleFrame = Frame(
        addProductsFrame,
        bg="#E6E6E6"
    )

    titleFrame.pack(
        fill="x",
        padx=30,
        pady=(15,10)
    )

    pageTitle = Label(
        titleFrame,
        text="Add Product",
        font=("Arimo", 28, "bold"),
        bg="#E6E6E6",
        fg="#1B1C1C"
    )

    pageTitle.pack(anchor="w")

    subtitleLabel = Label(
        titleFrame,
        text="Create and add a new product to inventory",
        font=("Arimo", 11),
        bg="#E6E6E6",
        fg="#6E6E6E"
    )

    subtitleLabel.pack(
        anchor="w",
        pady=(2,0)
    )

    divider = Frame(
        titleFrame,
        bg="#B0B0B0",
        height=1
    )

    divider.pack(
        fill="x",
        pady=(12,0)
    )

    # =========================
    # FORM CARD
    # =========================

    formCard = Frame(
        addProductsFrame,
        bg="#FFFFFF",
        bd=1,
        relief="solid"
    )

    formCard.pack(
        fill="x",
        padx=30,
        pady=10
    )

    # INNER FRAME

    innerFrame = Frame(
        formCard,
        bg="#FFFFFF"
    )

    innerFrame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    innerFrame.columnconfigure(1, weight=1)

    # PRODUCT NAME

    nameLabel = Label(
        innerFrame,
        text="Product Name",
        font=("Arimo", 11, "bold"),
        bg="#FFFFFF",
        fg="#1B1C1C"
    )

    nameLabel.grid(
        row=0,
        column=0,
        sticky="w",
        pady=8
    )

    nameEntry = Entry(
        innerFrame,
        font=("Arimo", 11)
    )

    nameEntry.grid(
        row=0,
        column=1,
        sticky="ew",
        padx=(25,0),
        ipady=5
    )

    # CATEGORY

    categoryLabel = Label(
        innerFrame,
        text="Category",
        font=("Arimo", 11, "bold"),
        bg="#FFFFFF",
        fg="#1B1C1C"
    )

    categoryLabel.grid(
        row=2,
        column=0,
        sticky="w",
        pady=8
    )

    categoryEntry = Entry(
        innerFrame,
        font=("Arimo", 11)
    )

    categoryEntry.grid(
        row=2,
        column=1,
        sticky="ew",
        padx=(25,0),
        ipady=5
    )

    # PRICE

    priceLabel = Label(
        innerFrame,
        text="Price",
        font=("Arimo", 11, "bold"),
        bg="#FFFFFF",
        fg="#1B1C1C"
    )

    priceLabel.grid(
        row=3,
        column=0,
        sticky="w",
        pady=8
    )

    priceEntry = Entry(
        innerFrame,
        font=("Arimo", 11)
    )

    priceEntry.grid(
        row=3,
        column=1,
        sticky="ew",
        padx=(25,0),
        ipady=5
    )

    # STOCK

    stockLabel = Label(
        innerFrame,
        text="Stock",
        font=("Arimo", 11, "bold"),
        bg="#FFFFFF",
        fg="#1B1C1C"
    )

    stockLabel.grid(
        row=4,
        column=0,
        sticky="w",
        pady=8
    )

    stockEntry = Entry(
        innerFrame,
        font=("Arimo", 11)
    )

    stockEntry.grid(
        row=4,
        column=1,
        sticky="ew",
        padx=(25,0),
        ipady=5
    )

    # =========================
    # BUTTON SECTION
    # =========================

    buttonFrame = Frame(
        addProductsFrame,
        bg="#E6E6E6"
    )

    buttonFrame.pack(
        fill="x",
        padx=30,
        pady=(5,20)
    )

    addBtn = Button(
        buttonFrame,
        text="+ Add Product",
        bg="#1C4975",
        fg="white",
        font=("Arimo", 12, "bold"),
        padx=18,
        pady=7,
        bd=0,
        cursor="hand2",
        command=addProduct
    )

    addBtn.pack(
        side="right"
    )
