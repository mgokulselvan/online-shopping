from database.exec import execute

def update_order_status(
    order_id,
    status
):

    query = """
        UPDATE orders
        SET status = :1
        WHERE order_id = :2
    """

    execute(
        query,
        [
            status,
            order_id
        ]
    )
