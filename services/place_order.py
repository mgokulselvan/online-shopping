from database.exec import execute
from services.cart_services import (
    get_cart,
    get_cart_total,
)
from services.validate_cart import validate_cart


def process_payment(user_id, payment_method):

    status, product, stock = validate_cart(user_id)

    if status == "stock_error":
        return ("stock_error", product, stock)

    cart_items = get_cart(user_id)

    if not cart_items:
        return ("empty_cart", None,None)

    total = get_cart_total(user_id)

    # CREATE ORDER
    execute(
        """
        INSERT INTO orders
        (
            user_id,
            status,
            total_amount
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
            "PLACED",
            total
        )
    )

    # GET CREATED ORDER ID
    result = execute(
        """
        SELECT MAX(order_id)
        FROM orders
        WHERE user_id = :1
        """,
        (user_id,),
        fetchone=True
    )

    order_id = result[0]

    # CREATE ORDER ITEMS
    # UPDATE STOCK
    for item in cart_items:

        product_id = item[1]
        price = item[4]
        quantity = item[5]

        execute(
            """
            INSERT INTO order_items
            (
                order_id,
                product_id,
                quantity,
                price
            )
            VALUES
            (
                :1,
                :2,
                :3,
                :4
            )
            """,
            (
                order_id,
                product_id,
                quantity,
                price
            )
        )

        execute(
            """
            UPDATE products
            SET stock_qty = stock_qty - :1
            WHERE product_id = :2
            """,
            (
                quantity,
                product_id
            )
        )

    # CREATE PAYMENT
    execute(
        """
        INSERT INTO payments
        (
            order_id,
            amount,
            method,
            status
        )
        VALUES
        (
            :1,
            :2,
            :3,
            :4
        )
        """,
        (
            order_id,
            total,
            payment_method,
            "SUCCESS"
        )
    )

    # CLEAR CART
    execute(
        """
        DELETE FROM cart
        WHERE user_id = :1
        """,
        (user_id,)
    )

    return ("success", order_id)
