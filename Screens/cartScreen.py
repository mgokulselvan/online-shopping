from tkinter import *
from tkinter import messagebox
from Components import itemCard,navbar
from services.cart_services import (get_cart,get_cart_total,update_cart_quantity)
from services.validate_cart import validate_cart
import sessionData

def cartScreen(root):

    cart_items = get_cart(
        sessionData.curr_user_id
    )

    total = get_cart_total(
        sessionData.curr_user_id
    )


    cartFrame = Frame(root, bg="#E6E6E6")
    cartFrame.pack(fill="both", expand=True)

    def saveCart():
        for cart_id, qty_var in cart_entries:
            new_qty = qty_var.get()

            status,data = update_cart_quantity(
                cart_id,
                new_qty
            )

            if status == "stock_error":

                messagebox.showerror(
                    "Stock Error",
                    f"Only {data} units available."
                )

                return

        messagebox.showinfo(
            "Success",
            "Cart updated successfully."
        )

        cartFrame.destroy()
        cartScreen(root)

    def gotoPayment():

        status, product, stock = validate_cart(
            sessionData.curr_user_id
        )

        if status == "stock_error":
            messagebox.showerror(
                "Stock Error",
                f"{product} only has {stock} units available."
            )
            return
        cartFrame.destroy()
        from .paymentScreen import paymentScreen
        paymentScreen(root)


    
    navbar(cartFrame,root)


    # PAGE TITLE
    cartTitle = Label(
        cartFrame,
        text="Shopping Cart",
        font=("Arimo", 20, "bold"),
        bg="#E6E6E6",
        fg="#1B1C1C"
    )

    cartTitle.pack(anchor="w", padx=20, pady=(20,10))


# BOTTOM BAR
    bottomBar = Frame(
        cartFrame,
        bg="#D9D9D9",
        height=70
    )

    bottomBar.pack(side="bottom", fill="x")

    bottomBar.pack_propagate(False)

# CONTENT INSIDE BAR
    bottomContent = Frame(
        bottomBar,
        bg="#D9D9D9"
    )

    bottomContent.pack(fill="both", expand=True, padx=20, pady=15)

    bottomContent.columnconfigure(0, weight=1)
    bottomContent.columnconfigure(1, weight=1)
    bottomContent.columnconfigure(2, weight=1)

# TOTAL LABEL
    totalLabel = Label(
        bottomContent,
        text=f"Total: ${total}",
        font=("Arimo", 16, "bold"),
        bg="#D9D9D9",
        fg="#1B1C1C"
    )

    totalLabel.grid(row=0, column=0, sticky="w")

# SAVE BUTTON
    saveBtn = Button(
        bottomContent,
        text="Save Cart",
        bg="#B0B0B0",
        fg="#1B1C1C",
        font=("Arimo", 11, "bold"),
        padx=15,
        pady=6,
        command=saveCart
    )

    saveBtn.grid(row=0, column=1,sticky="ew")

# BUY BUTTON
    buyBtn = Button(
        bottomContent,
        text="Buy Now",
        bg="#1C4975",
        fg="white",
        font=("Arimo", 12, "bold"),
        padx=20,
        pady=8,
        command=gotoPayment
    )

    buyBtn.grid(row=0, column=2, sticky="e")


    # CONTENT FRAME
    contentFrame = Frame(cartFrame, bg="#E6E6E6")
    contentFrame.pack(fill="both", expand=True)

    # SCROLLABLE CANVAS
    cartCanvas = Canvas(
        contentFrame,
        bg="#E6E6E6",
        highlightthickness=0
    )

    cartCanvas.pack(side="left", fill="both", expand=True)

    # SCROLLBAR
    scrollbar = Scrollbar(contentFrame, orient="vertical")
    scrollbar.pack(side="right", fill="y")

    scrollbar.config(command=cartCanvas.yview)
    cartCanvas.config(yscrollcommand=scrollbar.set)

    # INNER FRAME
    itemsFrame = Frame(cartCanvas, bg="#E6E6E6")

    canvasWindow = cartCanvas.create_window(
        (0,0),
        window=itemsFrame,
        anchor="nw"
    )

    itemsFrame.bind(
        "<Configure>",
        lambda e:
            cartCanvas.configure(
                scrollregion=cartCanvas.bbox("all")
            )
    )

    cartCanvas.bind(
        "<Configure>",
        lambda e:
            cartCanvas.itemconfig(
                canvasWindow,
                width=cartCanvas.winfo_width()
            )
    )

    cart_entries = []

    for item in cart_items:

        cart_id = item[0]
        product_id = item[1]
        product_name = item[2]
        category = item[3]
        price = item[4]
        quantity = item[5]
        subtotal = item[6]

        qty_var=itemCard(
            itemsFrame,
            product_name,
            category,
            price,
            quantity
        )

        cart_entries.append(
            (cart_id, qty_var)
        )

