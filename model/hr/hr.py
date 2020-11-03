""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util
from datetime import date #do obliczania ilości dni pomiędzy podaną datą
from datetime import datetime

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]

list_of_employee = data_manager.read_table_from_file(DATAFILE)

def add_employee(new_employee):
    list_of_employee.append(new_employee)
    data_manager.write_table_to_file(DATAFILE,list_of_employee)


def update_employee(employee_nr, updated_employee):
    list_of_employee[int(employee_nr)] = updated_employee
    data_manager.write_table_to_file(DATAFILE,list_of_employee)


def delete_employee(employee_to_delete):
    del list_of_employee[int(employee_to_delete)]
    data_manager.write_table_to_file(DATAFILE,list_of_employee)


def oldest_youngest_employee():
    date_of_birth = {}
    list_of_employees = data_manager.read_table_from_file(DATAFILE, separator=';')

    for employee in list_of_employees:
        date_of_birth[employee[1]] = datetime.strptime(employee[2], '%Y-%m-%d')

    today = datetime.today()
    youngest_emplyee = max(date_of_birth, key = lambda k: date_of_birth[k])
    oldest_emplyee = min(date_of_birth, key = lambda k: date_of_birth[k])
    youngest_emplyee_age = f'{(today.year - date_of_birth[youngest_emplyee].year)} years old'
    oldest_emplyee_age = f'{(today.year - date_of_birth[oldest_emplyee].year)} years old'

    return f'The oldest employee is {oldest_emplyee} ({oldest_emplyee_age}) and \
the youngest is {youngest_emplyee} ({youngest_emplyee_age}).'

def read_customers_list(): #odczyt musi być w funkcji aby każdorazowo odczytywał z pliku - bez funkcji odczyta tylko raz na początku programu 
    list_customers = data_manager.read_table_from_file(DATAFILE, separator=';')
    return list_customers

def employees_average(current_year):
    sum_of_years = 0
    counter = 0
    list_customers = data_manager.read_table_from_file(DATAFILE, separator=';') #wczytanie listy list z pliku hr.csv
    for customer in list_customers: #iterowanie kolejnych list z danymi
        counter+=1
        customer_year = (customer[2]) #pobranie komórki z datą [RRRR-MM-DD]
        customer_year = int(customer_year[0:4]) #wyodrębnienie roku [RRRR]
        sum_of_years += (current_year - customer_year) #sumowanie wieku kolejnych pracowników
        #input(str(sum_of_years))
    return round((sum_of_years/counter),0)  #średni wiek pracownika (total/ile_osob), round(x,0) - 0miejsc po przecinku

def employees_birthday(given_date):
    
   #wyodrębnienie poszczególnych danych z daty, date format: "2020-10-28"
    given_year = int(given_date[0:4])
    given_month = int(given_date[5:7])
    given_day = int(given_date[8:10])
    first_date = date(given_year, given_month, given_day) #przypisanie do zmiennej, biblioteka date umożliwia operacje na datach

    names = []

    list_customers = data_manager.read_table_from_file(DATAFILE, separator=';') #wczytanie listy list z pliku hr.csv
    for customer in list_customers: #iterowanie kolejnych list z danymi
        customer_date=customer[2]
        #customer_year = int(customer_date[0:4])
        customer_month = int(customer_date[5:7])
        customer_day = int(customer_date[8:10])

        last_date = date(given_year, customer_month,customer_day) #przypisanie do zmiennej, biblioteka date umożliwia operacje na datach
        delta = last_date - first_date #odejmowanie dat
        delta = delta.days #zamiana na ilość dni, typ int
        #input(str(delta))
        
        if (delta <= 14 and delta >=0) : # sprawdza czy urodziny kolejnych osób są w ciągu 2 tygodni od podanej daty
            names.append(customer[1]) #spisuje imiona osób, które mają urodziny w przeciągu 2tygodni

    return names

def count_employees_clerance(clerance):
    number_of_people = 0
    list_customers = data_manager.read_table_from_file(DATAFILE, separator=';') #wczytanie listy list z pliku hr.csv
    for customer in list_customers: #iterowanie kolejnych list z danymi
        if int(customer[4]) >= clerance:
            number_of_people +=1
    return number_of_people


def count_employees_department():
    departement_dict = {}
    list_customers = data_manager.read_table_from_file(DATAFILE, separator=';') #wczytanie listy list z pliku hr.csv
    for customer in list_customers: #iterowanie kolejnych list z danymi
        if customer[3] not in departement_dict: #sprawdza czy dany dział (customer[3]) już wcześniej siępojawił
            departement_dict[customer[3]] = int(customer[4]) #jeśli nie to tworzy nowy klucz i przypisuje mu wartość z pliku csv customer[4]
        else:
            departement_dict[customer[3]] += int(customer[4]) #jeśli dany dział (klucz) już jest w słowniku, to sumuje jego wartość

    return departement_dict



