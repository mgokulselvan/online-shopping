from database.exec import execute

def get_all_orders():

    query = """
        SELECT
            o.order_id,
            u.user_id,
            u.name,
            u.email,
            u.phone,
            u.address,
            p.payment_id,
            p.method,
            o.total_amount,
            o.status
        FROM orders o
        JOIN users u
            ON o.user_id = u.user_id
        JOIN payments p
            ON o.order_id = p.order_id
        ORDER BY o.order_date DESC
    """

    return execute(
        query,
        fetchall=True
    )

def get_order_items(order_id):
    query = """
        SELECT
            pr.product_name,
            oi.quantity,
            oi.price
        FROM order_items oi
        JOIN products pr
            ON oi.product_id = pr.product_id
        WHERE oi.order_id = :1
    """
    return execute(
        query,
        [order_id],
        fetchall=True
    )
