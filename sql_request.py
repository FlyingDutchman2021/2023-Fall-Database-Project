import _sql_request as db
import bcrypt as bc


def isEmail(entry: str):
    return db.isEmail(entry)


def isContactNumber(entry: str):
    return db.isContactNumber(entry)


def isID(entry: str):
    return db.isID(entry)


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
# error: Email Format, error: Contact Number Format, Success, SQL Error
def register_patient(_email: str, _name: str, _sex: str, _birth_date: str,
                     _blood_type: str, _contact_number: str, _note: str, password: str):
    # Check email, name, contact_number, note
    # Purify Everything
    if not db.isEmail(_email):
        return 'error: Email Format'
    if not db.isContactNumber(_contact_number):
        return 'error: Contact Number Format'
    _email = db.purify(_email)
    _name = db.purify(_name)
    _contact_number = db.purify(_contact_number)
    _note = db.purify(_note)

    # Turn str to int
    _birth_date = int(_birth_date)
    _contact_number = int(_contact_number)

    # Get id
    status, result = db.find_latest_entry('patient')
    _id = result[0][0]

    # Add Info
    status1, result_list1 = db.add_patient_info(_email, _name, _sex, _birth_date, _blood_type, _contact_number, _note)
    status2, result_list2 = db.add_password(_id, 'P', db.hash_new_password(password))
    if status1 == 'Success' and status2 == 'Success':
        return 'Success'
    else:
        return 'SQL Error'


# Return <status>
# possible status:
# error: Success, SQL Error
def delete_patient_account(_id: int):
    status1, result = db.delete_patient_info(_id)
    status2, result = db.delete_password(_id, 'P')
    if status1 == 'Success' and status2 == 'Success':
        return 'Success'
    else:
        return 'SQL Error'




def register_doctor():
    pass


def delete_doctor_account():
    pass


def register_nurse():
    pass


def delete_nurse_account():
    pass


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
    if status == 'Success':
        return status, result
    else:
        return 'SQL Error', []


# Return <status>
# possible status:
# error: Email Format, error: Contact Number Format, Success, SQL Error
def update_patient_info(_id: int, _email: str, _name: str, _sex: str, _birth_date: str,
                        _blood_type: str, _contact_number: str, _note: str):
    if not db.isEmail(_email):
        return 'error: Email Format'
    if not db.isContactNumber(_contact_number):
        return 'error: Contact Number Format'
    _email = db.purify(_email)
    _name = db.purify(_name)
    _contact_number = db.purify(_contact_number)
    _note = db.purify(_note)

    # Turn str to int
    _birth_date = int(_birth_date)
    _contact_number = int(_contact_number)

    # Add Info
    status, result = db.update_patient_info(_id, _email, _name, _sex, _birth_date, _blood_type, _contact_number, _note)
    if status == 'Success':
        return status
    else:
        return 'SQL Error'


def update_doctor_info():
    pass


def update_nurse_info():
    pass

