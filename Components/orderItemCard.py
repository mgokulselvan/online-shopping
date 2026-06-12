from tkinter import *

def orderItemCard(
    parentFrame,
    itemName,
    quantity
):

    itemFrame = Frame(
        parentFrame,
        bg="#FFFFFF",
        bd=1,
        relief="solid",
        padx=10,
        pady=10
    )

    itemFrame.pack(fill="x", pady=5)

    # ITEM NAME
    itemLabel = Label(
        itemFrame,
        text=f"Item: {itemName}",
        font=("Arimo", 12, "bold"),
        bg="#FFFFFF",
        fg="#1B1C1C"
    )

    itemLabel.pack(anchor="w")

    # QUANTITY
    quantityLabel = Label(
        itemFrame,
        text=f"Quantity: {quantity}",
        font=("Arimo", 10),
        bg="#FFFFFF"
    )

    quantityLabel.pack(anchor="w")
