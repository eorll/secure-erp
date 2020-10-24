""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]


###dopisane MatLeg
list_customers = data_manager.read_table_from_file(DATAFILE, separator=';')

def new_customer(new_customer):
    newID = util.generate_id() #wygenerowanie ID dla nowego użytkownika
    new_customer.insert(0,newID) #na pierwsze miejscie w liście new_customer przypisuje ID
    full_list = data_manager.read_table_from_file(DATAFILE, separator=';') #pobranie tego co aktualnie jest w pliku CSV
    full_list.append(new_customer) #dopisanie nowej lini do pliku CSV
    data_manager.write_table_to_file(DATAFILE, full_list) #zapis zaktualizowanej listy do pliku CSV
