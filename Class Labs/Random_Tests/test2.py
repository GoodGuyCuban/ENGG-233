def update_info(patient, doc_name, new_doc):
    new_age = patient[2] + 1
    patient[2] = new_age
    doc_name = new_doc

name = 'Morgan Lee'
health_num = '019A88D'
age = 36
doctor_name = 'Dr. Zarr'

patient_info = [health_num, name, age]

new_doctor = 'Dr. Maal'

update_info(patient_info, doctor_name, new_doctor)

print(patient_info)