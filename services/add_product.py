from database.exec import execute

def add_product(
    product_name,
    category,
    price,
    stock_qty
):

    query = """
        INSERT INTO products
        (
            product_name,
            category,
            price,
            stock_qty
        )
        VALUES
        (
            :1,
            :2,
            :3,
            :4
        )
    """

    execute(
        query,
        [
            product_name,
            category,
            price,
            stock_qty
        ]
    )
