import config
import sqlite3
import bcrypt as bc


# Purify a string for sql execution
# adding extra ' behind '
def purify(_input: str):
    _input = _input.strip()
    length = len(_input)
    where_we_need_extra_care: [int] = [0]
    for i in range(length):
        char = _input[i]
        if char == "'":
            where_we_need_extra_care.append(i + 1)
    where_we_need_extra_care.append(length)
    combined_result: str = ""
    for i in range(len(where_we_need_extra_care) - 1):
        start = where_we_need_extra_care[i]
        end = where_we_need_extra_care[i + 1]
        combined_result = combined_result + _input[start:end] + "'"
    combined_result = combined_result[0:len(combined_result) - 1]
    return combined_result


def isEmail(entry: str) -> bool:
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
def isContactNumber(entry: str) -> bool:
    if entry.isdigit() and len(entry) == 11:
        return True
    else:
        return False


# ID type: 12 digits
def isID(entry: str) -> bool:
    if entry.isdigit():
        if len(entry) == 12:
            return True
    return False


def _table_translate(table_kind: str) -> str:
    if table_kind == 'patient':
        return 'patient_info'
    elif table_kind == 'doctor':
        return 'doctor_info'
    elif table_kind == 'nurse':
        return 'nurse_info'
    else:
        print('table_translate_error')
        return ''


# Base sql request framework
# Return <status>, <result_list>
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

    except sqlite3.Error as err:
        err_msg = ' '.join(err.args)
        if dev_mode_on:
            print(err_msg)
        return err_msg, []


# Return <status>, <result_list>
def find_latest_entry(table: str):
    if table == 'patient':
        table = 'patient_info'
    elif table == 'doctor':
        table = 'doctor_info'
    elif table == 'nurse':
        table = 'nurse_info'
    else:
        return 'No such table', []
    sql = "SELECT seq from sqlite_sequence WHERE name = '%s'" % table
    return _sql_request(sql)


# Password
#
# Find password
# Add (including hashing)
# Update
# Delete
#
# Find password according to id and identity
#
# _id: 12 digits integer,
# _identity: string either be 'P', 'D' or 'N'
def find_password(_id: int, _identity: str):
    sql = "SELECT password From password WHERE id = %d AND identity = '%s'" % (_id, _identity)
    return _sql_request(sql)


def hash_new_password(_new_password: str) -> str:

    print(str(_new_password))

    pd = bytes(_new_password, 'utf-8')
    salt = bc.gensalt(config.salt_round)
    hpd = bc.hashpw(pd, salt)
    return hpd.decode('utf-8')


def add_password(_id: int, _identity: str, _password: str):
    sql = "INSERT INTO password (id, identity, password) VALUES (%d, '%s', '%s')" % (_id, _identity, _password)
    return _sql_request(sql)


def update_password(_id: int, _identity: str, _password: str):
    sql = "UPDATE password SET password = '%s' WHERE id = %d and identity = '%s'" % (_password, _id, _identity)
    return _sql_request(sql)


# _identity: P, D, or N
def delete_password(_id: int, _identity: str):
    sql = "DELETE FROM password WHERE id = %d and identity = '%s'" % (_id, _identity)
    return _sql_request(sql)


# Universal for Patient, Doctor and Nurse
#
# Show information (with start and range)
# Find information (with search key options: id or contact or email)
#
def show_info(_target_table: str, start: int, number_of_page: int):
    sql = "SELECT * FROM %s LIMIT %d OFFSET %d" % (_target_table, number_of_page, start - 1)
    return _sql_request(sql)


# _target_table: 'patient' or 'doctor' or 'nurse'
# _info: 'all', 'id'
# _search_by: 'id' or 'contact' or 'email'
# _search_key: just like it says! :)
def find_info(_target_table, _info: str, _search_by: str, _search_key):
    table: str = _table_translate(_target_table)
    info: str = ''
    search_sentence: str = ''

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


# Patient
#
# Add
# Edit (personal) [All]
# Delete

def add_patient_info(_email: str, _name: str, _sex: str, _birth_date: int,
                     _blood_type: str, _contact_number: int, _note: str = ''):
    sql = ("INSERT INTO patient_info (email, name, sex, birth_date, blood_type, contact_number, note) VALUES ('%s', "
           "'%s', '%s', %d, '%s', %d, '%s')") % (_email, _name, _sex, _birth_date, _blood_type, _contact_number, _note)
    return _sql_request(sql)


def update_patient_info(_id: int, _email: str, _name: str, _sex: str, _birth_date: int,
                        _blood_type: str, _contact_number: int, _note: str = ''):
    sql = ("UPDATE patient_info SET email = '%s', name = '%s', sex = '%s', birth_date = %d, "
           "blood_type = '%s', contact_number = %d, note = '%s' WHERE id = %d ") % (_email, _name, _sex,
                                                                                    _birth_date, _blood_type,
                                                                                    _contact_number, _note,
                                                                                    _id)
    return _sql_request(sql)


def delete_patient_info(_id: int):
    sql = "DELETE FROM patient_info WHERE id = %d" % _id
    return _sql_request(sql)


# Doctor
#
# Show pending (with start and range)
# Add
# Edit (personal)
# Edit (admin)
# Delete

def show_pending_doctor(start: int, number_of_page: int):
    sql = "SELECT * FROM doctor_info WHERE status='P' LIMIT %d OFFSET %d" % (number_of_page, start - 1)
    return _sql_request(sql)


def add_doctor_info(_email: str, _name: str, _sex: str, _contact_number: int, _department: str, _status: str):
    sql = ("INSERT INTO doctor_info (email, name, sex, contact_number, department, status) "
           "VALUES ('%s', '%s', '%s', %d, '%s', '%s')"
           % (_email, _name, _sex, _contact_number, _department, _status))
    return _sql_request(sql)


def update_doctor_info(_id: int, _email: str, _name: str, _sex: str, _contact_number: int):

    sql = ("UPDATE doctor_info SET email='%s', name='%s', sex='%s', contact_number=%d WHERE id=%d"
           % (_email, _name, _sex, _contact_number, _id))
    return _sql_request(sql)


def update_doctor_admin(_id: int, department: str, status: str):
    sql = "UPDATE doctor_info SET department='%s', status='%s' WHERE id=%d" % (department, status, _id)
    return _sql_request(sql)


def delete_doctor_info(_id: int):
    sql = "DELETE FROM doctor_info WHERE id = %d" % _id
    return _sql_request(sql)


# Nurse
#
# Show pending (with start and range)
# Add
# Edit (personal)
# Edit (Admin)
# Delete
#

def show_pending_nurse(start: int, number_of_page: int):
    sql = "SELECT * FROM nurse_info WHERE status='P' LIMIT %d OFFSET %d" % (number_of_page, start - 1)
    return _sql_request(sql)


def add_nurse_info(email: str, name: str, sex: str, contact_number: int, department: str, status: str, isMaster: int):
    sql = ("INSERT INTO nurse_info (email, name, sex, contact_number, department, status, isMaster) "
           "VALUES ('%s','%s','%s', %d, '%s', '%s', %d)") % (email, name, sex, contact_number, department,
                                                             status, isMaster)
    return _sql_request(sql)


def update_nurse_info(_id: int, email: str, name: str, sex: str, contact_number: int):
    sql = ("UPDATE nurse_info set email = '%s', name = '%s', sex = '%s', contact_number = %d "
           "WHERE id = %d") % (email, name, sex, contact_number, _id)
    return _sql_request(sql)


def update_nurse_admin(_id: int, department: str, status: str, isMaster: bool):
    isMaster = 1 if isMaster else 0
    sql = ("UPDATE nurse_info SET department='%s', status = '%s', isMaster=%d WHERE id = %d"
           % (department, status, isMaster, _id))
    return _sql_request(sql)


def delete_nurse_info(_id):
    sql = "DELETE FROM nurse_info WHERE id = %d" % _id
    return _sql_request(sql)


# 病房的操作
# 床位是否空闲
def check_bed_availability(room: int, bed: int):
    sql = "SELECT * FROM bed_assignment WHERE room = %d AND bed = %d AND patient_id IS NULL" % (room, bed)
    return _sql_request(sql)


# 将病人安置到指定床位
def assign_bed_to_patient(room: int, bed: int, patient_id: int):
    sql = "UPDATE bed_assignment SET patient_id = %d WHERE room = %d AND bed = %d" % (patient_id, room, bed)
    return _sql_request(sql)

# 处方的操作
def add_new_prescription(patient_id: int, doctor_id: int, date_time_created: int, content: str):
    sql = ("INSERT INTO prescriptions (patient_id, doctor_id, date_time_created, content) "
           "VALUES ('%s','%s','%s','%s')") % (patient_id,doctor_id,date_time_created,content)
    return _sql_request(sql)
