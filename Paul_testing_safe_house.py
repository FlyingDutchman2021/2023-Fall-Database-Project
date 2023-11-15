import sql_request as db

# print(db._add_patient_info('example3@mail.com', 'Mr.3', 'Male',
#                            20010103, 'Unknown', 15016984567,
#                            ' '))

# print(db._delete_patient_info(100000000003))
#
# options = {'email': 'example1@mail.com', 'sex': 'male'}
# option_keys = []
# option_values = []



print(db._update_patient_info(100000000001, sex='Male'))

