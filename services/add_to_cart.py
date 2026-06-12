from database.exec import execute

def add_to_cart(
    user_id,
    product_id,
    quantity
):

    stock_result = execute(
        """
        SELECT stock_qty
        FROM products
        WHERE product_id = :1
        """,
        (product_id,),
        fetchone=True
    )

    stock_qty = stock_result[0]

    existing = execute(
        """
        SELECT cart_id, quantity
        FROM cart
        WHERE user_id=:1
        AND product_id=:2
        """,
        (
            user_id,
            product_id
        ),
        fetchone=True
    )

    if existing:

        new_qty = existing[1] + quantity

        if new_qty> stock_qty:
            return("stock_error",stock_qty)
        execute(
            """
            UPDATE cart
            SET quantity = quantity + :1
            WHERE cart_id = :2
            """,
            (
                quantity,
                existing[0]
            )
        )

    else:
        if quantity>stock_qty:
            return("stock_error",stock_qty)

        execute(
            """
            INSERT INTO cart
            (
                user_id,
                product_id,
                quantity
            )
            VALUES
            (
                :1,
                :2,
                :3
            )
            """,
            (
                user_id,
                product_id,
                quantity
            )
        )

    return("added",None)
