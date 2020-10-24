""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]

def get_list_transaction():
    list_of_transaction = data_manager.read_table_from_file(DATAFILE)
    list_of_transaction.insert(0,HEADERS)
    return list_of_transaction

