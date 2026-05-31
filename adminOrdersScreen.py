from tkinter import *
from navbar import navbar
from orderAdminBox import orderAdminBox

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

    # SAMPLE ORDERS

    for i in range(10):

        orderAdminBox(
            ordersListFrame,
            f"ORD-{1000+i}",
            f"USR-{200+i}",
            f"User {i}",
            f"user{i}@mail.com",
            "9876543210",
            "New York, USA",
            f"PAY-{500+i}",
            "UPI",
            (i * 50) + 20,
            "PLACED"
        )
