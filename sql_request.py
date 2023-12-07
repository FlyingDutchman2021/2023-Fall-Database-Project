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
    #
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



def update_nurse_info(_id: int, email: str, name: str, sex: str, contact_number: str):
    if not db.isEmail(email):
        return 'error: Format'
    if not db.isContactNumber(contact_number):
        return 'error: Format'

    # 净化输入
    email = db.purify(email)
    name = db.purify(name)
    contact_number = int(db.purify(contact_number))

    # 更新信息
    status, result = db.update_nurse_info(_id, email, name, sex, contact_number)
    if status != 'Success':
        return 'SQL Error'

    return 'Success'


# 管理员对护士的修改
def update_nurse_admin(_id: int, department: str, status: str, isMaster: bool):

    # 更新状态
    status, result = db.update_nurse_status(_id, department, status, isMaster)
    if status != 'Success':
        return 'SQL Error'

    return 'Success'



# def update_nurse_password(_id: int, old_password: str, new_password: str):
#     # 确认旧密码的正确性
#     status1, result1 = db.find_password(_id,'N')
#     if status1 != 'Success':
#         return 'SQL Error'
#     stored_password = rtn_find_result[0][0]
#     if not bc.checkpw(old_password.encode('utf-8'), stored_password.encode('utf-8')):
#         return 'Wrong Password'
#
#     # 哈希处理新密码
#     hashed_password = db.hash_new_password(new_password)
#
#     # 更新密码
#     status, result = db.update_password(_id, 'N', hashed_password)
#     if status != 'Success':
#         return 'SQL Error'
#
#     return 'Success'

# 通用的修改密码
def update_password(_id: int, _identity: str, old_password: str, new_password: str):
    # 确认旧密码的正确性

    if _identity == 'nurse':
        identity = 'N'
    elif _identity == 'patient':
        identity = 'P'
    elif _identity == 'doctor':
        identity = 'D'

    status1, result1 = db.find_password(_id, identity)
    if status1 != 'Success':
        return 'SQL Error'
    stored_password = rtn_find_result[0][0]
    if not bc.checkpw(old_password.encode('utf-8'), stored_password.encode('utf-8')):
        return 'Wrong Password'

    # 哈希处理新密码
    hashed_password = db.hash_new_password(new_password)

    # 更新密码
    status, result = db.update_password(_id, 'N', hashed_password)
    if status != 'Success':
        return 'SQL Error'

    return 'Success'
# update doctor_info_status and etc
# search doctor
# search nurse
# search patient
# add test/prescription
# find test/prescription
# delete


def bed_assign(room: int, bed: int, patient_id: int):
    # 检查床位是否已被占用
    status, result = check_bed_availability(room, bed)
    if status != 'Success':
        return 'SQL Error'

    # 如果结果为空列表，表示床位可用
    if len(result) == 0:
        # 分配床位给病人
        status, assign_result = assign_bed_to_patient(room, bed, patient_id)
        if status != 'Success':
            return 'SQL Error'
        return 'Success'
    else:
        return 'Bed already occupied'

# 处方更新
def prescription_update(patient_id: int, doctor_id: int, content: str):
    # 获取当前系统时间并格式化为年月日时分的格式
    date_time_created = datetime.datetime.now().strftime("%Y%m%d%H%M")
    date_time_created = int(date_time_created)

    # 插入新的处方记录，并获取该记录的ID
    status, prescription_id = add_new_prescription(patient_id, doctor_id, date_time_created, content)
    if status != 'Success':
        return 'SQL Error'

    # 返回成功状态和处方ID
    return 'Success'