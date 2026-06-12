from tkinter import *
from Components import productCard,navbar
from services.fetch_products import get_all_products

def homeScreen(root):

    homeFrame = Frame(root,bg="#E6E6E6")
    homeFrame.pack(fill="both",expand=True)

    navbar(homeFrame,root)

    # SEARCH AREA
    searchFrame = Frame(homeFrame,bg="#D9D9D9")
    searchFrame.pack(side="top",padx=20)

    searchBox=Entry(searchFrame,width=30,font=("Arimo",10))
    searchBox.pack(side=LEFT,ipady=5)

    searchButton=Button(searchFrame,text="Search",bg="#1C4975",fg="white")
    searchButton.pack(side=LEFT,padx=5)


    # PRODUCTS SECTION

    #Making the products scrollable
    productsCanvas=Canvas(homeFrame,bg="#E6E6E6")
    productsCanvas.pack(side="left",fill="both",expand=True)

    #Scrollbar
    scrollbar=Scrollbar(homeFrame,orient="vertical")
    scrollbar.pack(side="right",fill="y")

    scrollbar.config(command=productsCanvas.yview)#it sets the yview function params automatically
    productsCanvas.config(yscrollcommand=scrollbar.set)#it sets the scrollbar.set function params automatically

    #UI container within Canvas
    productsFrame = Frame(productsCanvas,bg="#E6E6E6")

    canvasWindow = productsCanvas.create_window((0,0),window=productsFrame,anchor="nw")#drawing the frame within canvas

    productsFrame.bind(
        "<Configure>",
        lambda e:
            productsCanvas.configure(
                scrollregion=productsCanvas.bbox("all")
            )
    )

    productsCanvas.bind(
        "<Configure>",
        lambda e:
            productsCanvas.itemconfig(
                canvasWindow,
                width=productsCanvas.winfo_width()
            )
    )

    productsFrame.columnconfigure(0,weight=1)
    productsFrame.columnconfigure(1,weight=1)

#Fetching from DB
    products = get_all_products()

    for i, product in enumerate(products):

        productCard(
            productsFrame,
            i // 2,
            i % 2,
            product[0],
            product[1],           # product_name
            product[2],           # category
            product[3]            # price
        )



