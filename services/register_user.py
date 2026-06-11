from database.exec import execute


def register_user(
    name,
    email,
    phone,
    password,
    address
):

    existing = execute(
        """
        SELECT user_id
        FROM users
        WHERE email=:1
        """,
        (email,),
        fetchone=True
    )

    if existing:
        return False

    execute(
        """
        INSERT INTO users
        (
            name,
            email,
            phone,
            password,
            address
        )
        VALUES
        (
            :1,
            :2,
            :3,
            :4,
            :5
        )
        """,
        (
            name,
            email,
            phone,
            password,
            address
        )
    )

    return True
