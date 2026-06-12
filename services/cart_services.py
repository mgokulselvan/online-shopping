from database.exec import execute

def get_cart(user_id):
    query = """
        SELECT
            c.cart_id,
            c.product_id,
            p.product_name,
            p.category,
            p.price,
            c.quantity,
            (p.price * c.quantity) AS subtotal
        FROM cart c
        JOIN products p
            ON c.product_id = p.product_id
        WHERE c.user_id = :1
        ORDER BY c.cart_id
    """

    return execute(
        query,
        [user_id],
        fetchall=True
    )

def get_cart_total(user_id):
    query = """
        SELECT NVL(SUM(p.price * c.quantity),0)
        FROM cart c
        JOIN products p
            ON c.product_id = p.product_id
        WHERE c.user_id = :1
    """

    result = execute(
        query,
        [user_id],
        fetchall=True
    )

    return result[0][0]

def remove_cart_item(cart_id):
    query = """
        DELETE FROM cart
        WHERE cart_id = :1
    """

    execute(query, [cart_id])

def update_cart_quantity(cart_id, quantity):

    if quantity <= 0:
        remove_cart_item(cart_id)
        return("deleted",None)

    stock_query = """
        SELECT p.stock_qty
        FROM cart c
        JOIN products p
            ON c.product_id = p.product_id
        WHERE c.cart_id = :1
    """

    stock_result = execute(
        stock_query,
        [cart_id],
        fetchall=True
    )

    stock = stock_result[0][0]

    if quantity > stock:
        return ("stock_error", stock)

    update_query = """
        UPDATE cart
        SET quantity = :1
        WHERE cart_id = :2
    """

    execute(
        update_query,
        [quantity, cart_id]
    )

    return("Updated",None) 
