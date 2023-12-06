import _sql_request as db
import bcrypt as bc


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
        rtn_find_result = db.find_info(_identity, 'id', 'contact', contact_number)[1]
        if len(rtn_find_result) == 0:
            return 'User not found', 0
        else:
            uid = rtn_find_result[0][0]
    elif db.isID(_id_contact_email):
        uid = int(_id_contact_email)
    elif db.isEmail(_id_contact_email):
        email = _id_contact_email
        rtn_find_result = db.find_info(_identity, 'id', 'email', email)[1]
        if len(rtn_find_result) == 0:
            return 'User not found', 0
        else:
            uid = rtn_find_result[0][0]
    else:
        return 'Invalid username', 0

    rtn_find_result = db.find_password(uid, identity)[1]
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
    return db.find_info(_identity, 'all', 'id', _id)


def add_patient_info(_email: str, _name: str, _sex: str, _birth_date: str,
                     _blood_type: str, _contact_number: str, _note: str):
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

    # Add Info
    return db.add_patient_info(_email, _name, _sex, _birth_date, _blood_type, _contact_number, _note)


def delete_patient_info():
    pass


def update_patient_info():
    pass


def add_doctor_info():
    pass


def update_doctor_info():
    pass


def delete_doctor_info():
    pass


def add_nurse_info():
    pass


def update_nurse_info():
    pass


def delete_nurse_info():
    pass
