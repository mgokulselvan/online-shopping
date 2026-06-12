from tkinter import *
from services.update_product import update_product
from services.delete_product import delete_product

def inventoryItem(
    parentFrame,
    productId,
    productName,
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

    def updateItem():

        update_product(
            productId,
            priceVar.get(),
            stock.get()
        )
    def deleteItem():

        delete_product(productId)

        itemFrame.destroy()




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
        text="Price",
        font=("Arimo", 11, "bold"),
        bg="#FFFFFF",
        fg="#1B1C1C"
    )

    priceLabel.pack(anchor="w", pady=(5,0))

    priceVar = StringVar(value=str(price))

    priceBox = Entry(
        leftFrame,
        textvariable=priceVar,
        width=10,
        font=("Arimo", 11)
    )

    priceBox.pack(anchor="w", pady=(3,0))

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
        padx=10,
        command=updateItem
    )

    updateBtn.pack(side="left", padx=3)

    # DELETE BUTTON
    deleteBtn = Button(
        buttonFrame,
        text="Delete",
        bg="#B22222",
        fg="white",
        padx=10,
        command=deleteItem
    )

    deleteBtn.pack(side="left", padx=3)
