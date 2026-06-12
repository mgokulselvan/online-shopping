from database.exec import execute

def update_product(
    product_id,
    price,
    stock_qty
):

    query = """
        UPDATE products
        SET
            price = :1,
            stock_qty = :2
        WHERE product_id = :3
    """

    execute(
        query,
        [
            price,
            stock_qty,
            product_id
        ]
    )
