from database.exec import execute

def delete_product(product_id):

    query = """
        DELETE FROM products
        WHERE product_id = :1
    """

    execute(
        query,
        [product_id]
    )
