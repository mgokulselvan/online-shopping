from tkinter import *
from tkinter import messagebox
from Components import navbar
from services.place_order import process_payment
import sessionData

def paymentScreen(root):

    def pay():
        result=process_payment(
                sessionData.curr_user_id,
                paymentType.get()
                )
        if result[0] == "success":

            order_id = result[1]

            messagebox.showinfo(
                    "Payment Successful",
                    f"Order #{order_id} placed successfully."
                    )

            paymentFrame.destroy()

            from .homeScreen import homeScreen
            homeScreen(root)

        elif result[0] == "stock_error":

            product = result[1]
            stock = result[2]

            messagebox.showerror(
                    "Stock Error",
                    f"{product} only has {stock} units available."
                    )

        elif result[0] == "empty_cart":

            messagebox.showerror(
                    "Empty Cart",
                    "Your cart is empty."
                    )



    paymentFrame = Frame(root, bg="#E6E6E6")
    paymentFrame.pack(fill="both", expand=True)

    navbar(paymentFrame,root)

    # TITLE SECTION
    titleFrame = Frame(paymentFrame, bg="#E6E6E6")
    titleFrame.pack(fill="x", padx=20, pady=(20,10))

    paymentTitle = Label(
        titleFrame,
        text="Payment",
        font=("Arimo", 28, "bold"),
        fg="#1B1C1C",
        bg="#E6E6E6"
    )

    paymentTitle.pack(anchor="w")

    subtitleLabel = Label(
        titleFrame,
        text="Choose your payment method",
        font=("Arimo", 11),
        fg="#6E6E6E",
        bg="#E6E6E6"
    )

    subtitleLabel.pack(anchor="w", pady=(2,0))

    divider = Frame(
        titleFrame,
        bg="#B0B0B0",
        height=1
    )

    divider.pack(fill="x", pady=(12,0))

    # PAYMENT CARD
    paymentCard = Frame(
        paymentFrame,
        bg="#FFFFFF",
        bd=1,
        relief="solid",
        padx=20,
        pady=20
    )

    paymentCard.pack(fill="x", padx=20, pady=20)

    # PAYMENT METHOD TITLE
    paymentMethodLabel = Label(
        paymentCard,
        text="Payment Method",
        font=("Arimo", 14, "bold"),
        bg="#FFFFFF",
        fg="#1B1C1C"
    )

    paymentMethodLabel.pack(anchor="w", pady=(0,15))

    # PAYMENT METHOD VARIABLE
    paymentType = StringVar(value="UPI")

    # UPI
    upiBtn = Radiobutton(
        paymentCard,
        text="UPI",
        variable=paymentType,
        value="UPI",
        font=("Arimo", 11),
        bg="#FFFFFF"
    )

    upiBtn.pack(anchor="w", pady=3)

    # CARD
    cardBtn = Radiobutton(
        paymentCard,
        text="Credit / Debit Card",
        variable=paymentType,
        value="CARD",
        font=("Arimo", 11),
        bg="#FFFFFF"
    )

    cardBtn.pack(anchor="w", pady=3)

    # COD
    codBtn = Radiobutton(
        paymentCard,
        text="Cash on Delivery",
        variable=paymentType,
        value="COD",
        font=("Arimo", 11),
        bg="#FFFFFF"
    )

    codBtn.pack(anchor="w", pady=3)

    # CONFIRM BUTTON
    confirmBtn = Button(
        paymentFrame,
        text="Confirm Payment",
        bg="#1C4975",
        fg="white",
        font=("Arimo", 12, "bold"),
        padx=20,
        pady=8,
        command=pay
    )

    confirmBtn.pack(anchor="e", padx=20, pady=(0,20))
