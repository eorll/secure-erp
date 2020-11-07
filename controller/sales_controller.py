from model.sales import sales
from view import terminal as view
from model.crm import crm

def list_transactions():
    view.print_table(sales.list_of_transaction, sales.HEADERS)
    #view.get_input("Press enter")
    

def add_transaction():
    view.print_table(crm.read_customers_list(), crm.HEADERS)
    customer_nr = view.get_input("Enter customer number")
    new_transaction = view.get_inputs(sales.HEADERS[2:5])
    sales.add_transaction(new_transaction, customer_nr)
    view.get_input("Transaction added. Press enter")

def update_transaction():
    view.print_table(sales.list_of_transaction, sales.HEADERS)
    trancaction_to_update = view.get_input("Enter number of transaction to update")
    view.print_table(crm.read_customers_list(), crm.HEADERS)
    customer_nr = view.get_input("Enter customer number")
    updated_transaction = view.get_inputs(sales.HEADERS[2:5])
    sales.update_transaction(trancaction_to_update, updated_transaction, customer_nr)
    view.get_input("Transaction updated. Press enter")

def delete_transaction():
    view.print_menu("List of transactions: ", sales.list_of_transaction)
    trancaction_to_delete = view.get_input("Enter number of transaction to delete")
    sales.delete_transaction(trancaction_to_delete)
    view.get_input("Transaction deleted. Press enter")

def get_biggest_revenue_transaction():
    view.print_general_results(sales.biggest_revenue_transaction(), "Biggest revenue transaction is")
    view.get_input("\nPress enter")

def get_biggest_revenue_product():
    view.print_general_results(sales.biggest_revenue_product(), "Biggest revenue product is")
    view.get_input("\nPress enter")

def count_transactions_between():
    first_date = view.get_input("start date(YYYY-MM-DD) ")
    snd_date = view.get_input("end date(YYYY-MM-DD) ")
    view.print_general_results(sales.operation_between_transaction(first_date, snd_date)[0], "Number of transaction between is")
    view.get_input("\nPress enter")

def sum_transactions_between():
    first_date = view.get_input("start date(YYYY-MM-DD): ")
    snd_date = view.get_input("end date(YYYY-MM-DD): ")
    view.print_general_results(sales.operation_between_transaction(first_date, snd_date)[1], "Sum of transaction between is")
    view.get_input("\nPress enter")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)