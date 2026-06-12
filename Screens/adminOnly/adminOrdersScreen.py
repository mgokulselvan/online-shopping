from tkinter import *
from Components import navbar,adminOrdersContainer
from services.admin_orders import (
    get_all_orders,
    get_order_items
)


def adminOrdersScreen(root):

    ordersFrame = Frame(
        root,
        bg="#E6E6E6"
    )

    ordersFrame.pack(
        fill="both",
        expand=True
    )

    navbar(ordersFrame,root)

    # =========================
    # TITLE SECTION
    # =========================

    titleFrame = Frame(
        ordersFrame,
        bg="#E6E6E6"
    )

    titleFrame.pack(
        fill="x",
        padx=30,
        pady=(20,10)
    )

    ordersTitle = Label(
        titleFrame,
        text="Order Management",
        font=("Arimo", 28, "bold"),
        bg="#E6E6E6",
        fg="#1B1C1C"
    )

    ordersTitle.pack(anchor="w")

    subtitleLabel = Label(
        titleFrame,
        text="View and manage all customer orders",
        font=("Arimo", 11),
        bg="#E6E6E6",
        fg="#6E6E6E"
    )

    subtitleLabel.pack(anchor="w", pady=(2,0))

    divider = Frame(
        titleFrame,
        bg="#B0B0B0",
        height=1
    )

    divider.pack(fill="x", pady=(12,0))

    """
    # SEARCH AREA

    searchFrame = Frame(
        ordersFrame,
        bg="#D9D9D9"
    )

    searchFrame.pack(
        side="top",
        padx=20,
        anchor="w"
    )

    searchBox = Entry(
        searchFrame,
        width=30,
        font=("Arimo", 10)
    )

    searchBox.pack(
        side="left",
        ipady=5
    )

    searchBtn = Button(
        searchFrame,
        text="Search",
        bg="#1C4975",
        fg="white"
    )

    searchBtn.pack(
        side="left",
        padx=5
    )
    """
    # =========================
    # CONTENT FRAME
    # =========================

    contentFrame = Frame(
        ordersFrame,
        bg="#E6E6E6"
    )

    contentFrame.pack(
        fill="both",
        expand=True
    )

    # CANVAS

    ordersCanvas = Canvas(
        contentFrame,
        bg="#E6E6E6",
        highlightthickness=0
    )

    ordersCanvas.pack(
        side="left",
        fill="both",
        expand=True
    )

    # SCROLLBAR

    scrollbar = Scrollbar(
        contentFrame,
        orient="vertical"
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    scrollbar.config(command=ordersCanvas.yview)

    ordersCanvas.config(
        yscrollcommand=scrollbar.set
    )

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

    orders = get_all_orders()

    for order in orders:

        order_id = order[0]
        user_id = order[1]
        user_name = order[2]
        email = order[3]
        phone = order[4]
        address = order[5]
        payment_id = order[6]
        payment_type = order[7]
        total_amount = order[8]
        status = order[9]

        items = get_order_items(order_id)

        adminOrdersContainer(
            ordersListFrame,
            order_id,
            user_id,
            user_name,
            email,
            phone,
            address,
            payment_id,
            payment_type,
            total_amount,
            status,
            items
        )
