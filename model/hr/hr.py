""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""
from datetime import datetime
from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]

list_of_employees = data_manager.read_table_from_file(DATAFILE)


def oldest_youngest_employee():
    date_of_birth = {}

    for employee in list_of_employees:
        date_of_birth[employee[1]] = datetime.strptime(employee[2], '%Y-%m-%d')

    today = datetime.today()
    youngest_emplyee = max(date_of_birth, key = lambda k: date_of_birth[k])
    oldest_emplyee = min(date_of_birth, key = lambda k: date_of_birth[k])
    youngest_emplyee_age = f'{(today.year - date_of_birth[youngest_emplyee].year)} years old'
    oldest_emplyee_age = f'{(today.year - date_of_birth[oldest_emplyee].year)} years old'

    return f'The oldest employee is {oldest_emplyee} ({oldest_emplyee_age}) and \
the youngest is {youngest_emplyee} ({youngest_emplyee_age}).'