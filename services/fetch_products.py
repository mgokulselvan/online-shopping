from database.exec import execute

def get_all_products():

    return execute(
        """
        SELECT
            product_id,
            product_name,
            category,
            price,
            stock_qty
        FROM products
        ORDER BY product_id
        """,
        fetchall=True
    )
