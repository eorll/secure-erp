""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""
from model.crm import crm
from model import data_manager, util
from datetime import datetime
DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]

list_of_transaction = data_manager.read_table_from_file(DATAFILE)

def add_transaction(new_transaction, customer_nr):
    # adding transaction id
    new_transaction_final = [util.generate_id()]      
    # adding customer id
    new_transaction_final.extend([crm.list_customers[int(customer_nr) - 1][0]])  
    new_transaction_final.extend(new_transaction)
    list_of_transaction.append(new_transaction_final)
    data_manager.write_table_to_file(DATAFILE,list_of_transaction)


def update_transaction(transaction_nr, updated_transaction, customer_nr):
    updated_transaction_final = [util.generate_id()]      
    updated_transaction_final.extend([crm.list_customers[int(customer_nr) - 1][0]])  
    updated_transaction_final.extend(updated_transaction)
    list_of_transaction[int(transaction_nr) - 1] = updated_transaction_final
    data_manager.write_table_to_file(DATAFILE,list_of_transaction)


def delete_transaction(transaction_to_delete):
    del list_of_transaction[int(transaction_to_delete)]
    data_manager.write_table_to_file(DATAFILE,list_of_transaction)


def biggest_revenue_transaction():
    biggest_transaction = ["Id", "Customer", "Product", "0", "Date"]
    for transaction in list_of_transaction:
        if float(transaction[3]) > float(biggest_transaction[3]):
            biggest_transaction = transaction

    return biggest_transaction


def biggest_revenue_product():
    product_price = {}
    for transaction in list_of_transaction:
        if transaction[2] not in product_price:
            product_price[transaction[2]] = float(transaction[3]) #dodaje produkt z ceną do dict
        else:
            product_price[transaction[2]] += float(transaction[3]) #sumuje ceny tych samych produktów

    biggest_product = max(product_price, key = lambda k: product_price[k]) #najbardziej dochodowy produkt
    biggest_product_price = product_price[biggest_product] #dochód za ten produkt

    return [biggest_product, biggest_product_price]
    
    
def operation_between_transaction(date_1, date_2):
    date_1 = datetime.strptime(date_1, '%Y-%m-%d')
    date_2 = datetime.strptime(date_2, '%Y-%m-%d')
    number_of_transaction = 0
    sum_of_transaction = 0
    for transaction in list_of_transaction:
        transaction_date = datetime.strptime(transaction[4], '%Y-%m-%d') 
        if date_1 < transaction_date < date_2 :
            number_of_transaction += 1 # counts number of operation
            sum_of_transaction += float(transaction[3]) # sum of price between dates

    return number_of_transaction, sum_of_transaction

