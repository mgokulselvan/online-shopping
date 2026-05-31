from tkinter import *
from Components import orderContainer,navbar

def customerOrdersScreen(root):

    ordersFrame = Frame(root, bg="#E6E6E6")
    ordersFrame.pack(fill="both", expand=True)

    navbar(ordersFrame,root)
    # TITLE SECTION
    titleFrame = Frame(ordersFrame, bg="#E6E6E6")
    titleFrame.pack(fill="x", padx=20, pady=(20,10))

    ordersTitle = Label(
        titleFrame,
        text="Orders",
        font=("Arimo", 28, "bold"),
        fg="#1B1C1C",
        bg="#E6E6E6"
    )

    ordersTitle.pack(anchor="w")

    subtitleLabel = Label(
        titleFrame,
        text="Track all your previous orders",
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

    # CONTENT FRAME
    contentFrame = Frame(ordersFrame, bg="#E6E6E6")
    contentFrame.pack(fill="both", expand=True)

    # SCROLLABLE CANVAS
    ordersCanvas = Canvas(
        contentFrame,
        bg="#E6E6E6",
        highlightthickness=0
    )

    ordersCanvas.pack(side="left", fill="both", expand=True)

    # SCROLLBAR
    scrollbar = Scrollbar(contentFrame, orient="vertical")
    scrollbar.pack(side="right", fill="y")

    scrollbar.config(command=ordersCanvas.yview)
    ordersCanvas.config(yscrollcommand=scrollbar.set)

    # INNER FRAME
    ordersListFrame = Frame(
        ordersCanvas,
        bg="#E6E6E6"
    )

    canvasWindow = ordersCanvas.create_window(
        (0,0),
        window=ordersListFrame,
        anchor="nw"
    )

    ordersListFrame.bind(
        "<Configure>",
        lambda e:
            ordersCanvas.configure(
                scrollregion=ordersCanvas.bbox("all")
            )
    )

    ordersCanvas.bind(
        "<Configure>",
        lambda e:
            ordersCanvas.itemconfig(
                canvasWindow,
                width=ordersCanvas.winfo_width()
            )
    )

    # SAMPLE ORDERS
    orderContainer(
        ordersListFrame,
        "ORD-1021",
        "PLACED"
    )

    orderContainer(
        ordersListFrame,
        "ORD-2044",
        "SHIPPED"
    )

    orderContainer(
        ordersListFrame,
        "ORD-8821",
        "DELIVERED"
    )
