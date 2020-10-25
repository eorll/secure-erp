""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]
def get_employees():
     return [["Jz6J5&jw<r","Alice","2000-01-01","Sales","3"]['45+ohJm&dB','Bob','1989-10-13','Production','6']['ßl0W_tbm5Z','Cecil','1993-04-04','Sales','5']]
