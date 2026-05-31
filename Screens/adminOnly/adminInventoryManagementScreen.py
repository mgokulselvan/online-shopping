from tkinter import *
from Components import navbar,inventoryItem

def adminInventoryManagementScreen(root):

    inventoryFrame = Frame(root, bg="#E6E6E6")
    inventoryFrame.pack(fill="both", expand=True)

    navbar(inventoryFrame,root)

    def addProduct():
        inventoryFrame.destroy()
        from adminAddProductScreen import adminAddProductScreen
        adminAddProductScreen(root)


    # TITLE SECTION
    titleFrame = Frame(
        inventoryFrame,
        bg="#E6E6E6"
    )

    titleFrame.pack(
        fill="x",
        padx=20,
        pady=(20,10)
    )

    inventoryTitle = Label(
        titleFrame,
        text="Product Management",
        font=("Arimo", 28, "bold"),
        bg="#E6E6E6",
        fg="#1B1C1C"
    )

    inventoryTitle.pack(anchor="w")

    subtitleLabel = Label(
        titleFrame,
        text="Add, update, delete and manage products",
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
    secTopBar = Frame(
        titleFrame,
        bg="#E6E6E6",
    )

    secTopBar.pack(side="left", padx=20,ipady=5,ipadx=5,fill="x",expand=True)

    searchBox = Entry(
        secTopBar,
        width=30,
        font=("Arimo", 10)
    )

    searchBox.pack(side="left", ipady=8,anchor="w")

    searchBtn = Button(
        secTopBar,
        text="Search",
        bg="#1C4975",
        fg="white"
    )

    searchBtn.pack(side="left", padx=5, ipady=3,anchor="w")

    # ADD PRODUCT BUTTON
    addProductBtn = Button(
        secTopBar,
        text="Add Product",
        bg="#1C4975",
        fg="white",
        font=("Arimo", 11, "bold"),
        padx=15,
        pady=5,
        command=addProduct
    )

    addProductBtn.pack(anchor="e", pady=(10,0))

    # CONTENT FRAME
    contentFrame = Frame(
        inventoryFrame,
        bg="#E6E6E6"
    )

    contentFrame.pack(fill="both", expand=True)

    # CANVAS
    inventoryCanvas = Canvas(
        contentFrame,
        bg="#E6E6E6",
        highlightthickness=0
    )

    inventoryCanvas.pack(side="left", fill="both", expand=True)

    # SCROLLBAR
    scrollbar = Scrollbar(
        contentFrame,
        orient="vertical"
    )

    scrollbar.pack(side="right", fill="y")

    scrollbar.config(command=inventoryCanvas.yview)

    inventoryCanvas.config(
        yscrollcommand=scrollbar.set
    )

    # INNER FRAME
    inventoryListFrame = Frame(
        inventoryCanvas,
        bg="#E6E6E6"
    )

    canvasWindow = inventoryCanvas.create_window(
        (0,0),
        window=inventoryListFrame,
        anchor="nw"
    )

    inventoryListFrame.bind(
        "<Configure>",
        lambda e:
            inventoryCanvas.configure(
                scrollregion=inventoryCanvas.bbox("all")
            )
    )

    inventoryCanvas.bind(
        "<Configure>",
        lambda e:
            inventoryCanvas.itemconfig(
                canvasWindow,
                width=inventoryCanvas.winfo_width()
            )
    )

    # SAMPLE PRODUCTS
    for i in range(20):

        inventoryItem(
            inventoryListFrame,
            f"PRD-{1000+i}",
            f"Product {i}",
            f"Product {i} description",
            "Socks",
            (i * 10) + 5,
            i * 3
        )
