from tkinter import *

def itemCard(parentFrame, itemName, itemDesc, unitPrice, quantityValue):

    # ITEM CARD
    itemCard = Frame(
        parentFrame,
        bg="#E6E6E6",
        bd=1,
        relief="solid",
        padx=10,
        pady=10,
        height=120
    )

    itemCard.pack(fill="x", padx=10, pady=5)

    # LEFT + RIGHT CONTAINER
    contentFrame = Frame(itemCard, bg="#E6E6E6")
    contentFrame.pack(fill="x")

    # LEFT SECTION
    leftFrame = Frame(contentFrame, bg="#E6E6E6")
    leftFrame.pack(side="left", anchor="w")

    # ITEM NAME
    itemLabel = Label(
        leftFrame,
        text=itemName,
        font=("Arimo", 16, "bold"),
        bg="#E6E6E6",
        fg="#1C4975"
    )

    itemLabel.pack(anchor="w")

    # DESCRIPTION
    itemDescLabel = Label(
        leftFrame,
        text=itemDesc,
        font=("Arimo", 9),
        bg="#E6E6E6",
        fg="#919090"
    )

    itemDescLabel.pack(anchor="w", pady=(2,5))

    # UNIT PRICE
    priceLabel = Label(
        leftFrame,
        text=f"Unit Price: ${unitPrice}",
        font=("Arimo", 11, "bold"),
        bg="#E6E6E6",
        fg="#1B1C1C"
    )

    priceLabel.pack(anchor="w")

    # RIGHT SECTION
    rightFrame = Frame(contentFrame, bg="#E6E6E6")
    rightFrame.pack(side="right", anchor="e")

    quantityLabel = Label(
        rightFrame,
        text="Quantity",
        font=("Arimo", 10),
        bg="#E6E6E6",
        fg="#1B1C1C"
    )

    quantityLabel.pack(anchor="e")

    quantity = IntVar(value=quantityValue)

    quantityBox = Entry(
        rightFrame,
        textvariable=quantity,
        width=5,
        justify="center",
        font=("Arimo", 11)
    )

    quantityBox.pack(pady=(5,0), ipady=4)
