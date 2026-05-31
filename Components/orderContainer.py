from tkinter import *
from .orderItemCard import orderItemCard

def orderContainer(parentFrame, orderId, status):

    orderContainerFrame = Frame(
        parentFrame,
        bg="#EDEDED",
        bd=1,
        relief="solid",
        padx=15,
        pady=15
    )

    orderContainerFrame.pack(fill="x", padx=20, pady=10)

    # ORDER ID
    orderIdLabel = Label(
        orderContainerFrame,
        text=f"Order ID: {orderId}",
        font=("Arimo", 14, "bold"),
        bg="#EDEDED",
        fg="#1B1C1C"
    )

    orderIdLabel.pack(anchor="w")

    # STATUS
    statusLabel = Label(
        orderContainerFrame,
        text=f"Status: {status}",
        font=("Arimo", 11),
        bg="#EDEDED",
        fg="#1C4975"
    )

    statusLabel.pack(anchor="w", pady=(2,10))

    # SAMPLE ITEMS
    orderItemCard(
        orderContainerFrame,
        "Blue Socks",
        2,
        "UPI",
        20
    )

    orderItemCard(
        orderContainerFrame,
        "Black Socks",
        1,
        "COD",
        10
    )

# CANCEL BUTTON

    cancelBtn = Button(
        orderContainerFrame,
        text="Cancel Order",
        bg="#B22222",
        fg="white",
        padx=12
    )

    cancelBtn.pack(
        side="right",
        padx=(0,10)
    )
