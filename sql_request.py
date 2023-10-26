import sqlite3


def strip_sql(entry: str):
    entry = entry.strip()
    return entry


def validating(entry: str):
    for char in entry:
        if char == ' ':
            return False
    return True


def sql_request(SQL: str, db: str = 'hospital_system.db'):
    try:
        with sqlite3.connect(database=db) as db:
            temp_cursor = db.cursor()
            print(SQL)
            temp_cursor.execute(SQL)
            temp_result = temp_cursor.fetchall()
            temp_cursor.close()
            return 'Success', temp_result

    except sqlite3.Error:
        print(sqlite3.Error)
        return sqlite3.Error, ''


# sql = '''SELECT * FROM pending_doctor_info'''
# result = sql_request(sql)
# print(result)
s = 'shfdkalj  '
print(validating(strip_sql(s)))

