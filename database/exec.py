from database.connection import get_connection
def execute(query, params=None, fetchone=False, fetchall=False):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(query, params or ())

        if fetchone:
            return cursor.fetchone()

        if fetchall:
            return cursor.fetchall()

        conn.commit()
        return cursor.rowcount

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()
