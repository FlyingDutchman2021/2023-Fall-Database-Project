import sqlite3


# # Input a string, strip the blanks front and back
# def _strip_sql(entry: str):
#     entry = entry.strip()
#     return entry


# Validate an entry value. If a string contains any blank space, return False
#
def _isValid(entry: str):
    for char in entry:
        if char == ' ':
            return False
    return True


# Base sql request framework
# Return <status>, <result list>
# <status>:
# 'Success': The SQL is executed successfully
# <error>: The SQL can not be executed due to some database level error
#
# TODO dev_mode_on
def _sql_request(SQL: str, db: str = 'hospital_system.db', dev_mode_on=True):
    try:
        with sqlite3.connect(database=db) as db:
            temp_cursor = db.cursor()
            if dev_mode_on:
                print(SQL)
            temp_cursor.execute(SQL)
            temp_result = temp_cursor.fetchall()
            temp_cursor.close()
            return 'Success', temp_result

    except sqlite3.Error:
        return sqlite3.Error, []


# Find password according to id and type
# Only return password
# @para _id: 12 digits integer,
# _type: string either be 'P', 'D' or 'N'
#
def _find_password_id(_id: int, _type: str):
    sql = "SELECT password From password WHERE id = %d AND type = '%s'" % (_id, _type)
    return _sql_request(sql)


# Tested
# Find patient info using id
# Return email, name, sex, birthdate, blood type, contact number, and notes
def _find_patient_info(_id: int):
    sql = '''SELECT * FROM patient_info WHERE id = %d''' % _id
    return _sql_request(sql)

#
#
# Public functions
#
#


# Return <status>
# 'Success': successfully log in to the system
# 'User not found': no such user exists
# 'Wrong Password': password is wrong
# 'Illegal username': username is illegal
# 'Invalid username': username is not any one of id, contact number or email
#
def login(_id_phone_email: str, _password: str, _identity: str):
    _id_phone_email = _id_phone_email.strip()
    _password = _password.strip()
    if not _isValid(_id_phone_email):
        return 'Illegal username'

    if _id_phone_email.isdigit():
        if len(_id_phone_email) == 11:
            phone_number = int(_id_phone_email)
            # TODO Phone Number search
        elif len(_id_phone_email) == 12:
            id = int(_id_phone_email)
            # TODO id search
        else:
            return 'Invalid username'
    elif '@' in _id_phone_email:
        email = _id_phone_email
        # TODO email search
    else:
        return 'Invalid username'


print(0)









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

