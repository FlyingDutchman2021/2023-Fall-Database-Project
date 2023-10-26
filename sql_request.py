import sqlite3


def sql_request(db: str, sql: str):
    try:
        with sqlite3.connect(database=db) as db:
            temp_cursor = db.cursor()
            print(sql)
            temp_cursor.execute(sql)
            temp_result = temp_cursor.fetchall()
            temp_cursor.close()
            return 'Success', temp_result

    except sqlite3.Error:
        print(sqlite3.Error)
        return sqlite3.Error, ''
