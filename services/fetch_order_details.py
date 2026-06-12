from database.exec import execute

def get_orders(user_id):

    query = """
        SELECT
            o.order_id,
            o.status,
            p.method,
            o.total_amount
        FROM orders o
        JOIN payments p
            ON o.order_id = p.order_id
        WHERE o.user_id = :1
        ORDER BY o.order_date DESC
    """

    return execute(
        query,
        [user_id],
        fetchall=True
    )

def get_order_items(order_id):

    query = """
        SELECT
            p.product_name,
            oi.quantity
        FROM order_items oi
        JOIN products p
            ON oi.product_id = p.product_id
        WHERE oi.order_id = :1
    """

    return execute(
        query,
        [order_id],
        fetchall=True
    )
