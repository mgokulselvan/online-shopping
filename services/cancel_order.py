from database.exec import execute

def cancel_order(order_id):

    query = """
        UPDATE orders
        SET status = 'CANCELLED'
        WHERE order_id = :1
    """

    execute(
        query,
        [order_id]
    )
