from tkinter import *

def adminItemOrderContainer(
    parentFrame,
    itemName,
    quantity,
    price
):

    itemFrame = Frame(
        parentFrame,
        bg="#FFFFFF",
        bd=1,
        relief="solid",
        padx=10,
        pady=10
    )

    itemFrame.pack(
        fill="x",
        pady=5
    )

    itemLabel = Label(
        itemFrame,
        text=f"Item: {itemName}",
        font=("Arimo", 12, "bold"),
        bg="#FFFFFF"
    )

    itemLabel.pack(anchor="w")

    quantityLabel = Label(
        itemFrame,
        text=f"Quantity: {quantity}",
        font=("Arimo", 10),
        bg="#FFFFFF"
    )

    quantityLabel.pack(anchor="w")

    priceLabel = Label(
        itemFrame,
        text=f"Price: ${price}",
        font=("Arimo", 10),
        bg="#FFFFFF"
    )

    priceLabel.pack(anchor="w")
