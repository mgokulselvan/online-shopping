from database.exec import execute

def validate_cart(user_id):

    query = """
        SELECT
            p.product_name,
            c.quantity,
            p.stock_qty
        FROM cart c
        JOIN products p
            ON c.product_id = p.product_id
        WHERE c.user_id = :1
    """

    items = execute(
        query,
        [user_id],
        fetchall=True
    )

    for item in items:

        product_name = item[0]
        cart_qty = item[1]
        stock_qty = item[2]

        if cart_qty > stock_qty:

            return (
                "stock_error",
                product_name,
                stock_qty
            )

    return ("valid", None, None)
