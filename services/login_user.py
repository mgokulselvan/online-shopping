from database.exec import execute

def login_user(
    email,
    password
):

    user = execute(
        """
        SELECT user_id,name,email,password,phone,address
        FROM users
        WHERE email=:1
        """,
        (email,),
        fetchone=True
    )

    if not user:
        return None

    if user[3]!=password:
        return None

    return user
