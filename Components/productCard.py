from tkinter import *
from tkinter import messagebox
import sessionData 
from services.add_to_cart import add_to_cart

def productCard(productsFrame,rowNo,colNo,productID,productName,productDesc,productPrice):

    #Add to cart button functionality
    def addItem():

        status,data=add_to_cart(
            sessionData.curr_user_id,
            productID,
            quantity.get()
        )
        if status=="stock_error":
            messagebox.showerror(
                    "Stock Error",
                    f"Only {data} units available"
                    )
            return
        messagebox.showinfo(
                "Success",
                "Added to cart"
                )

    # PRODUCT CARD
    #relief is the border style
    productCard = Frame(productsFrame,bg="#E6E6E6",bd=1,relief="solid",padx=10,pady=10,height=150)
    productCard.grid(row=rowNo,column=colNo,padx=5,pady=5,sticky="ew")


    #Product Name
    productLabel=Label(productCard,text=productName,font=("Arimo", 16, "bold"),bg="#E6E6E6",fg="#1C4975")
    productLabel.pack(side="top",anchor="w")


    #Product Description
    productDescLabel=Label(productCard,text=productDesc,font=("Arimo",9),bg="#E6E6E6",fg="#919090")
    productDescLabel.pack(side="top",anchor="w")


    #bottom - includes price and add to cart button
    bottomBarFrame=Frame(productCard,bg="#E6E6E6")
    bottomBarFrame.pack(side="bottom",fill="x")


    #price
    priceLabel=Label(bottomBarFrame,text=f"${productPrice}",font=("Arimo",14,"bold"),bg="#E6E6E6",fg="#1C4975")
    priceLabel.pack(side="left",anchor="w")

    #add to chart 
    addToCartBtn=Button(bottomBarFrame,text="Add",bg="#1C4975",fg="#E6E6E6",command=addItem)
    addToCartBtn.pack(side="right",anchor="e")

    #Quantity of items
    quantity = IntVar(value=1)

    quantityBox = Entry(
        bottomBarFrame,
        textvariable=quantity,
        width=3
    )
    quantityBox.pack(side="right",anchor="w",ipady=4,ipadx=4,padx=10)
