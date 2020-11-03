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
def read_customers_list(): #odczyt musi być w funkcji aby każdorazowo odczytywał z pliku - bez funkcji odczyta tylko raz na początku programu 
    list_customers = data_manager.read_table_from_file(DATAFILE, separator=';')
    return list_customers
#list_customers = data_manager.read_table_from_file(DATAFILE, separator=';')

def new_customer(new_customer,option=0):
    newID = util.generate_id() #wygenerowanie ID dla nowego użytkownika
    new_customer[0] = newID #na pierwsze miejscie w liście new_customer nadpisuje ID
    list_customers = data_manager.read_table_from_file(DATAFILE, separator=';') #pobranie tego co aktualnie jest w pliku CSV
    if option==0:
        #input("Option" + str(option))
        list_customers.append(new_customer) #dopisanie nowej lini do pliku CSV
    
    elif option > 0: #update
        option -= 1
        list_customers[option] = new_customer #nadpisuje dany wiersz nowymi wartościami podanymi przez użytkownika
        #input("UPDATED!")
    
    elif option < 0: #remove, minus oznacza że będziemy usuwac
        index = abs(option) -1 #zamiana na liczbę dodatnią = odczytanie numeru wiersza do usunięcia, -1 bo w tabeli wiersz 0d 0
        list_customers.pop(index) #usunięcie wybranego wiersza
        #input("REMOVED!")

    data_manager.write_table_to_file(DATAFILE, list_customers) #zapis zaktualizowanej listy do pliku CSV

def get_emails():
    subscribed_emails = []
    list_customers = data_manager.read_table_from_file(DATAFILE, separator=';') #pobranie tego co aktualnie jest w pliku CSV
    for customer in list_customers:  #szuka w liście klientów któzy subskrybują i dodaje ich emaile do nowej list
        if int(customer[3]) > 0:
            subscribed_emails.append(customer[2]) 
    return subscribed_emails