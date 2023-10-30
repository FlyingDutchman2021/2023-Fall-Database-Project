import sqlite3


#Tested
def strip_sql(entry: str):
    entry = entry.strip()
    return entry


# Tested
def validating(entry: str):
    for char in entry:
        if char == ' ':
            return False
    return True


# Tested
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


# Tested
# Find password according to id
def find_password(_id: int):
    sql = '''SELECT password From password WHERE id = %d''' % _id
    return sql_request(sql)


def find_patient_info(_id: int):
    sql = '''SELECT * FROM patient_info WHERE id = %d''' % _id
    return sql_request(sql)

# sql = '''SELECT * FROM pending_doctor_info'''


# id = 10001
# password = 'sakhjf;jaskdjf;j'
# sql = '''INSERT INTO password (id, password) VALUES (%d, '%s')''' % (id, password)


# id = 10001
# sql = '''SELECT * From password WHERE id = %d''' % id

# sql = '''SELECT * From pending_doctor_info'''

# table = 'password'
# sql = '''SELECT * From %s''' % table
# result = sql_request(sql)
# print(result)

