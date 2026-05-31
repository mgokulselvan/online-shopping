from tkinter import *

def inventoryItem(
    parentFrame,
    productId,
    productName,
    productDesc,
    category,
    price,
    stockValue
):

    itemFrame = Frame(
        parentFrame,
        bg="#FFFFFF",
        bd=1,
        relief="solid",
        padx=15,
        pady=15
    )

    itemFrame.pack(fill="x", padx=20, pady=8)

    # TOP SECTION
    topFrame = Frame(itemFrame, bg="#FFFFFF")
    topFrame.pack(fill="x")

    # LEFT SECTION
    leftFrame = Frame(topFrame, bg="#FFFFFF")
    leftFrame.pack(side="left", anchor="w")

    # PRODUCT NAME
    nameLabel = Label(
        leftFrame,
        text=productName,
        font=("Arimo", 15, "bold"),
        bg="#FFFFFF",
        fg="#1C4975"
    )

    nameLabel.pack(anchor="w")

    # PRODUCT ID
    idLabel = Label(
        leftFrame,
        text=f"Product ID: {productId}",
        font=("Arimo", 10),
        bg="#FFFFFF",
        fg="#6E6E6E"
    )

    idLabel.pack(anchor="w")

    # DESCRIPTION
    descLabel = Label(
        leftFrame,
        text=productDesc,
        font=("Arimo", 10),
        bg="#FFFFFF",
        fg="#1B1C1C"
    )

    descLabel.pack(anchor="w", pady=(5,0))

    # CATEGORY
    categoryLabel = Label(
        leftFrame,
        text=f"Category: {category}",
        font=("Arimo", 10),
        bg="#FFFFFF",
        fg="#1B1C1C"
    )

    categoryLabel.pack(anchor="w", pady=(5,0))

    # PRICE
    priceLabel = Label(
        leftFrame,
        text=f"Price: ${price}",
        font=("Arimo", 10),
        bg="#FFFFFF",
        fg="#1B1C1C"
    )

    priceLabel.pack(anchor="w", pady=(5,0))

    # RIGHT SECTION
    rightFrame = Frame(topFrame, bg="#FFFFFF")
    rightFrame.pack(side="right", anchor="e")

    # STOCK LABEL
    stockLabel = Label(
        rightFrame,
        text="Stock",
        font=("Arimo", 11, "bold"),
        bg="#FFFFFF",
        fg="#1B1C1C"
    )

    stockLabel.pack()

    stock = IntVar(value=stockValue)

    stockBox = Entry(
        rightFrame,
        textvariable=stock,
        width=6,
        justify="center",
        font=("Arimo", 11)
    )

    stockBox.pack(ipady=4, pady=(5,10))

    # BUTTONS FRAME
    buttonFrame = Frame(
        rightFrame,
        bg="#FFFFFF"
    )

    buttonFrame.pack()

    # UPDATE BUTTON
    updateBtn = Button(
        buttonFrame,
        text="Update",
        bg="#1C4975",
        fg="white",
        padx=10
    )

    updateBtn.pack(side="left", padx=3)

    # DELETE BUTTON
    deleteBtn = Button(
        buttonFrame,
        text="Delete",
        bg="#B22222",
        fg="white",
        padx=10
    )

    deleteBtn.pack(side="left", padx=3)
