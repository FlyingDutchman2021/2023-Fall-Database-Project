import config
import sqlite3
import bcrypt as bc


#
#
# Checking Session
# Checking the input from entry box
#
#


# Purify a string for sql execution
# adding extra ' behind '
def _purify(_input: str):
    _input = _input.strip()
    length = len(_input)
    where_we_need_extra_care: [int] = [0]
    for i in range(length):
        char = _input[i]
        if char == "'":
            where_we_need_extra_care.append(i+1)
    where_we_need_extra_care.append(length)
    combined_result: str = ""
    for i in range(len(where_we_need_extra_care)-1):
        start = where_we_need_extra_care[i]
        end = where_we_need_extra_care[i+1]
        combined_result = combined_result + _input[start:end] + "'"
    combined_result = combined_result[0:len(combined_result)-1]
    return combined_result




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
    # Verify the front part
    for i in range(1):
        start_point = 0
        end_point = key_position[0]
        if end_point - start_point < 1:
            return False
        for j in range(start_point, end_point):
            char = entry[j]
            print(char)
            if char.isspace():
                return False
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


# contact number type: 11 digits
def _isContactNumber(entry: str) -> bool:
    if entry.isdigit() and len(entry) == 11:
        return True
    else:
        return False


# ID type: 12 digits
def _isID(entry: str) -> bool:
    if entry.isdigit():
        if len(entry) == 12:
            return True
    return False


#
#
# SQL Request Session
# Where stores all the SQL codes
#
#


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


# Find password according to id and identity
# Only return password
# @para
# _id: 12 digits integer,
# _identity: string either be 'P', 'D' or 'N'
#
def _find_password(_id: int, _identity: str):
    sql = "SELECT password From password WHERE id = %d AND identity = '%s'" % (_id, _identity)
    return _sql_request(sql)


def _hash_new_password(_new_password: str) -> str:
    pd = bytes(_new_password, 'utf-8')
    salt = bc.gensalt(config.salt_round)
    hpd = bc.hashpw(pd, salt)
    return hpd.decode('utf-8')


def _add_password(_id: int, _identity: str, _password: str):
    sql = "INSERT INTO password (id, identity, password) VALUES (%d, '%s', '%s')" % (_id, _identity, _password)
    return _sql_request(sql)


def _delete_password(_id: int, _identity: str):
    sql = "DELETE FROM password WHERE id = %d and identity = '%s'" % (_id, _identity)
    return _sql_request(sql)


def _update_password(_id: int, _identity: str, _password: str):
    sql = "UPDATE password SET password = '%s' WHERE id = %d and identity = '%s'" % (_password, _id, _identity)
    return _sql_request(sql)


# _target_table: 'patient' or 'doctor' or 'nurse'
# _info: 'all', 'id'
# _search_by: 'id' or 'contact' or 'email'
# _search_key: just like it says! :)
def _find_info(_target_table, _info: str, _search_by: str, _search_key: str | int):
    table: str = ''
    info: str = ''
    search_sentence: str = ''

    if _target_table == 'patient':
        table = 'patient_info'
    elif _target_table == 'doctor':
        table = 'doctor_info'
    elif _target_table == 'nurse':
        table = 'nurse_info'
    else:
        print('_find_info_target_table_error')

    if _info == 'all':
        info = '*'
    elif _info == 'id':
        info = 'id'
    else:
        print('_find_info_info_error')

    if _search_by == 'id':
        search_sentence = "id = %d" % _search_key
    elif _search_by == 'contact':
        search_sentence = "contact_number = %d" % _search_key
    elif _search_by == 'email':
        search_sentence = "email = '%s'" % _search_key
    else:
        print('_find_info_search_by_error')

    sql = "SELECT %s FROM %s WHERE %s" % (info, table, search_sentence)
    return _sql_request(sql)


def _add_patient_info(_email: str, _name: str, _sex: str, _birth_date: int,
                      _blood_type: str, _contact_number: int, _note: str = ''):
    sql = ("INSERT INTO patient_info (email, name, sex, birth_date, blood_type, contact_number, note) VALUES ('%s', "
           "'%s', '%s', %d, '%s', %d, '%s')") % (_email, _name, _sex, _birth_date, _blood_type, _contact_number, _note)
    return _sql_request(sql)


def _delete_patient_info(_id: int):
    sql = "DELETE FROM patient_info WHERE id = %d" % _id
    return _sql_request(sql)


def _update_patient_info(_id: int, _email: str, _name: str, _sex: str, _birth_date: int,
                         _blood_type: str, _contact_number: int, _note: str = ''):
    sql = ("UPDATE patient_info SET email = '%s', name = '%s', sex = '%s', birth_date = %d, "
           "blood_type = '%s', contact_number = %d, note = '%s' WHERE id = %d ") % (_email, _name, _sex,
                                                                                    _birth_date, _blood_type,
                                                                                    _contact_number, _note,
                                                                                    _id)
    return _sql_request(sql)


def login(_id_contact_email: str, _password: str, _identity: str) -> (str, int):
    _id_contact_email = _purify(_id_contact_email)
    _password = _purify(_password)

    identity: str = ''
    if _identity == 'patient':
        identity = 'P'
    elif _identity == 'doctor':
        identity = 'D'
    elif _identity == 'nurse':
        identity = 'N'

    if _isContactNumber(_id_contact_email):
        contact_number = int(_id_contact_email)
        rtn_find_result = _find_info(_identity, 'id', 'contact', contact_number)[1]
        if len(rtn_find_result) == 0:
            return 'User not found', 0
        else:
            uid = rtn_find_result[0][0]
    elif _isID(_id_contact_email):
        uid = int(_id_contact_email)
    elif _isEmail(_id_contact_email):
        email = _id_contact_email
        rtn_find_result = _find_info(_identity, 'id', 'email', email)[1]
        if len(rtn_find_result) == 0:
            return 'User not found', 0
        else:
            uid = rtn_find_result[0][0]
    else:
        return 'Invalid username', 0

    rtn_find_result = _find_password(uid, identity)[1]
    if len(rtn_find_result) == 0:
        return 'User not found', 0
    else:
        stored_password = rtn_find_result[0][0]
    if bc.checkpw(_password.encode('utf-8'), stored_password.encode('utf-8')):
        return 'Success', uid
    else:
        return 'Wrong Password', 0


# Get personal info using user ID and identity
# _id: user ID
# _identity: can either be 'patient', 'doctor' or 'nurse'
def get_personal_info(_id: int, _identity: str):
    search_result = _find_info(_identity, 'all', 'id', _id)
    if not search_result[0] == 'Success':
        print('SQL error')
    result_list = search_result[1]
    if len(result_list) == 0:
        print('User not found')
    return result_list[0]


def add_patient_info(_email: str, _name: str, _sex: str, _birth_date: str,
                     _blood_type: str, _contact_number: str, _note: str):
    # Check email, name, contact_number, note
    # Purify Everything
    if not _isEmail(_email):
        return
    if not _isContactNumber(_contact_number):
        return
    _email = _purify(_email)
    _name = _purify(_name)
    _contact_number = _purify(_contact_number)
    _note = _purify(_note)
