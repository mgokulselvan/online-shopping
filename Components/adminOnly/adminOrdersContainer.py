from tkinter import *
from .adminItemOrderContainer import adminItemOrderContainer
from services.update_order_status import update_order_status

def adminOrdersContainer(
    parentFrame,
    orderId,
    userId,
    userName,
    email,
    phone,
    address,
    paymentId,
    paymentType,
    totalAmount,
    status,
    items
):

    orderFrame = Frame(
        parentFrame,
        bg="#FFFFFF",
        bd=1,
        relief="solid",
        padx=20,
        pady=20
    )

    orderFrame.pack(
        fill="x",
        padx=20,
        pady=10
    )


    def changeStatus():

        update_order_status(
            orderId,
            statusVar.get()
        )

        statusLabel.config(
            text=f"Status: {statusVar.get()}"
        )


    # =========================
    # ORDER INFO
    # =========================

    orderTitle = Label(
        orderFrame,
        text=f"Order ID: {orderId}",
        font=("Arimo", 16, "bold"),
        bg="#FFFFFF",
        fg="#1C4975"
    )

    orderTitle.pack(anchor="w")

    statusLabel = Label(
        orderFrame,
        text=f"Status: {status}",
        font=("Arimo", 10, "bold"),
        bg="#FFFFFF",
        fg="#1C4975"
    )

    statusLabel.pack(anchor="w")
    userIdLabel = Label(
        orderFrame,
        text=f"User ID: {userId}",
        font=("Arimo", 10),
        bg="#FFFFFF"
    )

    userIdLabel.pack(anchor="w", pady=(2,10))

    # =========================
    # USER DETAILS
    # =========================

    userTitle = Label(
        orderFrame,
        text="User Details",
        font=("Arimo", 12, "bold"),
        bg="#FFFFFF"
    )

    userTitle.pack(anchor="w")

    nameLabel = Label(
        orderFrame,
        text=f"Name: {userName}",
        font=("Arimo", 10),
        bg="#FFFFFF"
    )

    nameLabel.pack(anchor="w")

    emailLabel = Label(
        orderFrame,
        text=f"Email: {email}",
        font=("Arimo", 10),
        bg="#FFFFFF"
    )

    emailLabel.pack(anchor="w")

    phoneLabel = Label(
        orderFrame,
        text=f"Phone: {phone}",
        font=("Arimo", 10),
        bg="#FFFFFF"
    )

    phoneLabel.pack(anchor="w")

    addressLabel = Label(
        orderFrame,
        text=f"Address: {address}",
        font=("Arimo", 10),
        bg="#FFFFFF"
    )

    addressLabel.pack(anchor="w", pady=(0,10))

    # =========================
    # PAYMENT DETAILS
    # =========================

    paymentTitle = Label(
        orderFrame,
        text="Payment Details",
        font=("Arimo", 12, "bold"),
        bg="#FFFFFF"
    )

    paymentTitle.pack(anchor="w")

    paymentIdLabel = Label(
        orderFrame,
        text=f"Payment ID: {paymentId}",
        font=("Arimo", 10),
        bg="#FFFFFF"
    )

    paymentIdLabel.pack(anchor="w")

    paymentTypeLabel = Label(
        orderFrame,
        text=f"Payment Type: {paymentType}",
        font=("Arimo", 10),
        bg="#FFFFFF"
    )

    paymentTypeLabel.pack(anchor="w")

    totalLabel = Label(
        orderFrame,
        text=f"Total Amount: ${totalAmount}",
        font=("Arimo", 10),
        bg="#FFFFFF"
    )

    totalLabel.pack(anchor="w", pady=(0,10))

    # =========================
    # ORDER ITEMS
    # =========================

    itemsTitle = Label(
        orderFrame,
        text="Ordered Items",
        font=("Arimo", 12, "bold"),
        bg="#FFFFFF"
    )

    itemsTitle.pack(anchor="w")

    itemsFrame = Frame(
        orderFrame,
        bg="#FFFFFF"
    )

    itemsFrame.pack(fill="x", pady=(5,10))

    for item in items:

        product_name = item[0]
        quantity = item[1]
        price = item[2]

        adminItemOrderContainer(
            itemsFrame,
            product_name,
            quantity,
            price
        )
    # =========================
    # STATUS SECTION
    # =========================

    bottomFrame = Frame(
        orderFrame,
        bg="#FFFFFF"
    )

    bottomFrame.pack(fill="x", pady=(10,0))

    statusTitleLabel = Label(
        bottomFrame,
        text="Status",
        font=("Arimo", 11, "bold"),
        bg="#FFFFFF"
    )

    statusTitleLabel.pack(side="left")

    statusVar = StringVar(value=status)

    statusMenu = OptionMenu(
        bottomFrame,
        statusVar,
        "PLACED",
        "SHIPPED",
        "DELIVERED",
        "CANCELLED"
    )

    statusMenu.pack(side="left", padx=10)

    updateBtn = Button(
        bottomFrame,
        text="Update Status",
        bg="#1C4975",
        fg="white",
        padx=12,
        command=changeStatus
    )

    updateBtn.pack(side="right")


