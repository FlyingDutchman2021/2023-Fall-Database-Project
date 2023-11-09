import sqlite3


# @Invalid scenarios
# blank space or " or '
# Consecutive dash symbol --
def _isValid(entry: str) -> bool:
    for i in range(len(entry)):
        char = entry[i]
        if char == ' ' or char == '"' or char == "'":
            return False
        if char == '-':
            if i < len(entry) - 1:
                if entry[i + 1] == '-':
                    return False

    return True


def _isEmail(entry: str) -> bool:
    length = len(entry)
    key_position: [int] = []
    for i in range(length):
        current_char = entry[i]
        if len(key_position) == 0:
            if current_char == '@':
                key_position.append(i)
        else:
            if current_char == '.':
                key_position.append(i)

    if len(key_position) < 2:
        return False

    # Verify the legality of each part
    # Verify the middle parts
    for i in range(len(key_position) - 1):
        start_point = key_position[i] + 1
        end_point = key_position[i + 1]
        # Check if there is any content between the two key id thing
        # If there is no content, it's not valid and terminate the validating process
        # If there is any content ok, continue to check if it is valid
        if end_point - start_point < 1:
            return False
        # Check if the content is valid
        # If not, return false, terminate the validating process
        # If yes, continue to check the last part
        for j in range(start_point, end_point):
            char = entry[j]
            if not char.isalnum():
                return False

    # Check the last part
    for i in range(1):
        final_dot_position = key_position.pop()
        # Check if there is at least 2 following characters behind the last dot
        if len(entry) - final_dot_position < 3:
            return False
        # Check if it is all alphabets
        for j in range(final_dot_position + 1, len(entry)):
            char = entry[j]
            if not char.isalpha():
                return False

    # Checking done:
    # We have an @ symbol, and we can find at least one dot after the @
    # we have some content (alphabets or numbers) between the symbols
    # The trailing parts are all alphabets and is at least 2 characters long
    # All the checking is done, nothing wrong detected,so it is a valid email address!
    return True


def _isContactNumber(entry: str) -> bool:
    if entry.isdigit() and len(entry) == 11:
        return True
    else:
        return False


def _isID(entry: str) -> bool:
    if entry.isdigit():
        if len(entry) == 12:
            return True
    return False


# For Patient, Doctor, Nurse separately? idk

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
# @para
# _id: 12 digits integer,
# _type: string either be 'P', 'D' or 'N'
#
def _find_password_id(_id: int, _type: str):
    sql = "SELECT password From password WHERE id = %d AND type = '%s'" % (_id, _type)
    return _sql_request(sql)


# Find patient info using id (unique and primary key)
# Return email, name, sex, birthdate, blood type, contact number, and notes
def _find_patient_info_id(_id: int):
    sql = "SELECT * FROM patient_info WHERE id = %d" % _id
    return _sql_request(sql)


# Find patient info using contact number (unique)
# Return email, name, sex, birthdate, blood type, contact number, and notes
def _find_patient_info_contact_number(_contact_number: int):
    sql = "SELECT * FROM patient_info WHERE contact_number = %d" % _contact_number
    return _sql_request(sql)


# Find patient info using email (unique)
# Return email, name, sex, birthdate, blood type, contact number, and notes
def _find_patient_info_email(_email: str):
    sql = "SELECT * FROM patient_info WHERE email = '%s'" % _email
    return _sql_request(sql)


#
#
# Public functions
#
#

# TODO return one more thing: current user id (some may just have contact number or email address)
# Return <status>
# 'Success': successfully log in to the system
# 'User not found': no such user exists
# 'Wrong Password': password is wrong
# 'Illegal username': username is illegal, containing some inputs that is not allowed for sql search
# 'Invalid username': username is not any one of id, contact number or email
#
def login(_id_phone_email: str, _password: str, _identity: str):
    _id_phone_email = _id_phone_email.strip()
    if not _isValid(_id_phone_email):
        return 'Illegal username'

    if _isContactNumber(_id_phone_email):
        phone_number = int(_id_phone_email)
        # TODO Phone Number search
    elif _isID(_id_phone_email):
        id = int(_id_phone_email)
        # TODO id search
    elif _isEmail(_id_phone_email):
        email = _id_phone_email
        # TODO email search
    else:
        return 'Invalid username'
