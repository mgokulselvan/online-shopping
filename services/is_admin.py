from database.exec import execute

def is_admin(user_id):

    query = """
        SELECT admin_id
        FROM admins
        WHERE admin_id = :1
    """

    result = execute(
        query,
        [user_id],
        fetchone=True
    )
    
    return result is not None
