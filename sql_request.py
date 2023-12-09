import _sql_request as db
import bcrypt as bc
import datetime
import sqlite3


def isEmail(entry: str):
    return db.isEmail(entry)


def isContactNumber(entry: str):
    return db.isContactNumber(entry)


def isID(entry: str):
    return db.isID(entry)


# Universal Login for Patient, Doctor and Nurse (you have to indicate the identity)
#
# Return <status>, possible status:
# SQL Error, User not found, Invalid username, Success, Wrong Password
def login(_id_contact_email: str, _password: str, _identity: str) -> (str, int):
    _id_contact_email = db.purify(_id_contact_email)
    _password = db.purify(_password)

    identity: str = ''
    if _identity == 'patient':
        identity = 'P'
    elif _identity == 'doctor':
        identity = 'D'
    elif _identity == 'nurse':
        identity = 'N'

    if db.isContactNumber(_id_contact_email):
        contact_number = int(_id_contact_email)
        status, rtn_find_result = db.find_info(_identity, 'id', 'contact', contact_number)
        if not status == 'Success':
            return 'SQL Error', 0
        if len(rtn_find_result) == 0:
            return 'User not found', 0
        else:
            uid = rtn_find_result[0][0]
    elif db.isID(_id_contact_email):
        uid = int(_id_contact_email)
    elif db.isEmail(_id_contact_email):
        email = _id_contact_email
        status, rtn_find_result = db.find_info(_identity, 'id', 'email', email)
        if not status == 'Success':
            return 'SQL Error', 0
        if len(rtn_find_result) == 0:
            return 'User not found', 0
        else:
            uid = rtn_find_result[0][0]
    else:
        return 'Invalid username', 0

    status, rtn_find_result = db.find_password(uid, identity)
    if not status == 'Success':
        return 'SQL Error', 0
    if len(rtn_find_result) == 0:
        return 'User not found', 0
    else:
        stored_password = rtn_find_result[0][0]
    if bc.checkpw(_password.encode('utf-8'), stored_password.encode('utf-8')):
        return 'Success', uid
    else:
        return 'Wrong Password', 0


# Return <status>, possible status:
# error: Format, Success, SQL Error
def register_patient(_email: str, _name: str, _sex: str, _birth_date: str,
                     _blood_type: str, _contact_number: str, _note: str, password: str):
    # Check email, name, contact_number, note
    # Purify Everything
    if not db.isEmail(_email):
        return 'error: Format'
    if not db.isContactNumber(_contact_number):
        return 'error: Format'
    _email = db.purify(_email)
    _name = db.purify(_name)
    _note = db.purify(_note)
    # Turn str to int
    _birth_date = int(_birth_date)
    _contact_number = int(_contact_number)

    # Add Info
    status1, result_list1 = db.add_patient_info(_email, _name, _sex, _birth_date, _blood_type, _contact_number, _note)
    if not status1 == 'Success':
        return 'SQL Error'
    status2, result_list2 = db.find_latest_entry('patient')
    if not status2 == 'Success':
        return 'SQL Error'
    _id = result_list2[0][0]
    status3, result_list3 = db.add_password(_id, 'P', db.hash_new_password(password))
    if not status3 == 'Success':
        return 'SQL Error'
    return 'Success'


# Return <status>
# possible status:
# error: Success, SQL Error
def delete_patient_account(_id: int):
    status1, result = db.delete_patient_info(_id)
    if not status1 == 'Success':
        return 'SQL Error'
    status2, result = db.delete_password(_id, 'P')
    if not status2 == 'Success':
        return 'SQL Error'
    return 'Success'


def register_doctor(email: str, name: str, sex: str, contact_number: str, password: str):
    # Check entry inputs
    if not db.isEmail(email):
        return 'error: Format'
    if not db.isContactNumber(contact_number):
        return 'error: Format'
    # Purify them
    email = db.purify(email)
    name = db.purify(name)
    contact_number = int(contact_number)

    # Add Info
    status1, result_list1 = db.add_doctor_info(email, name, sex, contact_number, '', 'P')
    if not status1 == 'Success':
        return 'SQL Error'
    status2, result_list2 = db.find_latest_entry('doctor')
    if not status2 == 'Success':
        return 'SQL Error'
    _id = result_list2[0][0]
    status3, result_list3 = db.add_password(_id, 'D', db.hash_new_password(password))
    if not status3 == 'Success':
        return 'SQL Error'
    return 'Success'


def delete_doctor_account(_id: int):
    status1, result1 = db.delete_doctor_info(_id)
    if not status1 == 'Success':
        return 'SQL Error'
    status2, result2 = db.delete_password(_id, 'D')
    if not status2 == 'Success':
        return 'SQL Error'
    return 'Success'


def register_nurse(email: str, name: str, sex: str, contact_number: str, password: str):
    if not db.isEmail(email):
        return 'error: Format'
    if not db.isContactNumber(contact_number):
        return 'error: Format'
    email = db.purify(email)
    name = db.purify(name)
    contact_number = int(contact_number)
    status1, result1 = db.add_nurse_info(email, name, sex, contact_number, '', 'P', 0)
    if not status1 == 'Success':
        return 'SQL Error'
    status2, result2 = db.find_latest_entry('nurse')
    if not status2 == 'Success':
        return 'SQL Error'
    _id = result2[0][0]
    status3, result3 = db.add_password(_id, 'N', db.hash_new_password(password))
    if not status3 == 'Success':
        return 'SQL Error'
    return 'Success'


def delete_nurse_account(_id: int):
    status1, result1 = db.delete_nurse_info(_id)
    if not status1 == 'Success':
        return 'SQL Error'
    status2, result2 = db.delete_password(_id, 'N')
    if not status2 == 'Success':
        return 'SQL Error'
    return 'Success'


# Get personal info using user ID and identity
#
# _id: user ID
# _identity: can either be 'patient', 'doctor' or 'nurse'
#
# Return <status>, <list_of_result>
# possible status:
# Success, SQL Error
def get_personal_info(_id: int, _identity: str):
    status, result = db.find_info(_identity, 'all', 'id', _id)
    if not status == 'Success':
        return 'SQL Error', []
    return 'Success', result


# Universal
# 删除了旧密码确认
def update_password(_id: int, _identity: str, new_password: str):
    # 确认旧密码的正确性
    identity = ''
    if _identity == 'nurse':
        identity = 'N'
    elif _identity == 'patient':
        identity = 'P'
    elif _identity == 'doctor':
        identity = 'D'

    # status1, result1 = db.find_password(_id, identity)
    # if not status1 == 'Success':
    #     return 'SQL Error'
    # stored_password = result1[0][0]
    # if not bc.checkpw(old_password.encode('utf-8'), stored_password.encode('utf-8')):
    #     return 'Wrong Password'

    # 哈希处理新密码
    hashed_password = db.hash_new_password(new_password)
    # 更新密码
    status, result = db.update_password(_id, identity, hashed_password)
    if not status == 'Success':
        return 'SQL Error'
    return 'Success'


# Return <status>
# possible status:
# error: Email Format, error: Contact Number Format, Success, SQL Error
def update_patient_general(_id: int, _email: str, _name: str, _sex: str, _birth_date: str,
                           _blood_type: str, _contact_number: str, _note: str):
    if not db.isEmail(_email):
        return 'error: Format'
    if not db.isContactNumber(_contact_number):
        return 'error: Format'
    _email = db.purify(_email)
    _name = db.purify(_name)
    _note = db.purify(_note)
    _birth_date = int(_birth_date)
    _contact_number = int(_contact_number)

    # Add Info
    status, result = db.update_patient_info(_id, _email, _name, _sex, _birth_date, _blood_type, _contact_number, _note)
    if not status == 'Success':
        return 'SQL Error'
    return 'Success'


def update_doctor_general(_id: int, email: str, name: str, sex: str, contact_number: str):
    # Check entry inputs
    if not db.isEmail(email):
        return 'error: Format'
    if not db.isContactNumber(contact_number):
        return 'error: Format'
    # Purify them
    email = db.purify(email)
    name = db.purify(name)
    contact_number = int(contact_number)

    # Update Info
    status1, result_list1 = db.update_doctor_info(_id, email, name, sex, contact_number)
    if not status1 == 'Success':
        return 'SQL Error'
    return 'Success'


def update_doctor_admin(_id: int, department: str, status: str):
    status, result = db.update_doctor_admin(_id, department, status)
    if not status == 'Success':
        return 'SQL Error'
    return 'Success'


def update_nurse_general(_id: int, email: str, name: str, sex: str, contact_number: str):
    if not db.isEmail(email):
        return 'error: Format'
    if not db.isContactNumber(contact_number):
        return 'error: Format'
    # 净化输入
    email = db.purify(email)
    name = db.purify(name)
    contact_number = int(contact_number)
    # 更新信息
    status, result = db.update_nurse_info(_id, email, name, sex, contact_number)
    if not status == 'Success':
        return 'SQL Error'
    return 'Success'


def update_nurse_admin(_id: int, department: str, status: str, isMaster: bool):
    status, result = db.update_nurse_admin(_id, department, status, isMaster)
    if not status == 'Success':
        return 'SQL Error'
    return 'Success'


# Universal Search
#
#
def universal_find_patient(search_key: str):
    if search_key == '':
        sql = "SELECT * FROM patient_info"
    elif search_key.isdigit():
        # is digit action
        search_key = search_key + '%'
        sql = ("SELECT * FROM patient_info WHERE contact_number LIKE '%s' OR id LIKE '%s' OR email LIKE '%s'"
               % (search_key, search_key, search_key))
    else:
        # is mixed text action
        search_key = search_key + '%'
        search_key_name = '%' + search_key + '%'
        sql = ("SELECT * FROM patient_info WHERE name LIKE '%s' OR email LIKE '%s'"
               % (search_key_name, search_key))
    status, result = db._sql_request(sql)
    if not status == 'Success':
        return 'SQL Error', []
    return 'Success', result


# status: if you don't want to filter anything, leave it blank
#         but if you want to filter the pending(P) or accepted(A) ones,
#         enter 'P' or 'A'.
def universal_find_doctor(search_key: str, status: str = ''):
    sql = ''
    if search_key == '':
        pass
    elif search_key.isdigit():
        # is digit action
        search_key = search_key + '%'
        sql = ("SELECT * FROM doctor_info WHERE (contact_number LIKE '%s' OR id LIKE '%s' OR email LIKE '%s')"
               % (search_key, search_key, search_key))
    else:
        # is mixed text action
        search_key = search_key + '%'
        search_key_name = '%' + search_key + '%'
        sql = ("SELECT * FROM doctor_info WHERE (name LIKE '%s' OR email LIKE '%s' OR department LIKE '%s')"
               % (search_key_name, search_key, search_key))

    if status == '':
        if sql == '':
            sql = "SELECT * FROM doctor_info"
    elif status == 'P':
        if sql == '':
            sql = "SELECT * FROM doctor_info WHERE status='P'"
        else:
            sql = sql + " AND status='P'"
    elif status == 'A':
        if sql == '':
            sql = "SELECT * FROM doctor_info WHERE status='A'"
        else:
            sql = sql + " AND status='A'"
    else:
        print('status value illegal!!!')
    status, result = db._sql_request(sql)
    if not status == 'Success':
        return 'SQL Error', []
    return 'Success', result


# status: if you don't want to filter anything, leave it blank
#         but if you want to filter the pending(P) or accepted(A) ones,
#         enter 'P' or 'A'.
#
# isMaster: if you want to filter the Master nurse, turn it to True,
#           otherwise leave it there, don't touch it, it has default value.
def universal_find_nurse(search_key: str, status: str = '', isMaster: bool = False):
    sql = ''
    if search_key == '' and status == '' and isMaster == False:
        sql = "SELECT * FROM nurse_info"
    if search_key == '':
        pass
    elif search_key.isdigit():
        # is digit action
        search_key = search_key + '%'
        sql = ("SELECT * FROM nurse_info WHERE (contact_number LIKE '%s' OR id LIKE '%s' OR email LIKE '%s')"
               % (search_key, search_key, search_key))
    else:
        # is mixed text action
        search_key = search_key + '%'
        search_key_name = '%' + search_key + '%'
        sql = ("SELECT * FROM nurse_info WHERE (name LIKE '%s' OR email LIKE '%s' OR department LIKE '%s')"
               % (search_key_name, search_key, search_key))

    if status == '':
        pass
    elif status == 'P':
        if sql == '':
            sql = "SELECT * FROM nurse_info WHERE status='P'"
        else:
            sql = sql + " AND status='P'"
    elif status == 'A':
        if sql == '':
            sql = "SELECT * FROM nurse_info WHERE status='A'"
        else:
            sql = sql + " AND status='A'"
    else:
        print('status value illegal!!!')

    if isMaster is True:
        if sql == '':
            sql = "SELECT * FROM nurse_info WHERE isMaster=1"
        else:
            sql = sql + " AND isMaster=1"

    status, result = db._sql_request(sql)
    if not status == 'Success':
        return 'SQL Error', []
    return 'Success', result


# find prescription: using patient id to find his/her prescriptions (optional: order)
# delete

# find room assignment: using patient id to find room and bed / using room to find its patient
# delete

# add nurse assignment
# find nurse assignment: using nurse id to find the room he / she is in charge of/ using room id
# to find the assigned nurse delete

# Optional 挂号表 patient id and doctor id, time
# 挂号即添加记录， 看完就删
# 医生能看到挂他号的病人， 病人能看到他挂了谁的号： find using patient id / doctor id

def bed_assign(room: int, bed: int, patient_id: int):
    # 检查床位是否已被占用
    status, result = db.check_bed_availability(room, bed)
    if not status == 'Success':
        return 'SQL Error'

    # 如果结果为空列表，表示床位可用
    if len(result) == 0:
        # 分配床位给病人
        status, assign_result = db.assign_bed_to_patient(room, bed, patient_id)
        if not status == 'Success':
            return 'SQL Error'
        return 'Success'
    else:
        return 'Bed already occupied'


# Find medical records based on patient ID
def find_medical(patient_id: str):
    sql = ("SELECT * FROM prescriptions WHERE patient_id = %s" % patient_id)
    status, result = db._sql_request(sql)
    if not status == 'Success':
        return 'SQL Error', []
    return 'Success', result


# 处方更新
def prescription_update(patient_id: int, doctor_id: int, content: str):
    # 获取当前系统时间并格式化为年月日时分的格式
    date_time_created = datetime.datetime.now().strftime("%Y%m%d%H%M")
    date_time_created = int(date_time_created)

    # 插入新的处方记录，并获取该记录的ID
    status, prescription_id = db.add_new_prescription(patient_id, doctor_id, date_time_created, content)
    if status != 'Success':
        return 'SQL Error'

    # 返回成功状态和处方ID
    return 'Success'


# Find the ward based on nurse_id
def find_nurse_ward(nurse_id: str):
    sql = ("SELECT * FROM nurse_assignment WHERE nurse_id = %s" % nurse_id)
    status, result = db._sql_request(sql)
    if not status == 'Success':
        return 'SQL Error', []
    return 'Success', result


# Find the nurse based on room_id
def find_ward_nurse(room_id: str):
    sql = ("SELECT * FROM nurse_assignment WHERE room_id = %s" % room_id)
    status, result = db._sql_request(sql)
    if not status == 'Success':
        return 'SQL Error', []
    return 'Success', result


# Assign ward
def assign_ward(nurse_id: int, room_id: int):
    sql = ("UPDATE nurse_assignment SET room_id = %d WHERE nurse_id = %d "
           % (room_id, nurse_id))
    return db._sql_request(sql)
