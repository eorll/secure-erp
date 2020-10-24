from model.crm import crm
from view import terminal as view


def list_customers():
    #view.print_error_message("Not implemented yet.")
    view.print_table(crm.list_customers)
    input("OK")


def add_customer():
    #view.print_error_message("Not implemented yet.")
    add_c = view.get_inputs(crm.HEADERS) #pobieranie danych od użytkownika
    crm.new_customer(add_c)
    input("OK")


def update_customer():
    view.print_error_message("Not implemented yet.")
    input("OK")


def delete_customer():
    view.print_error_message("Not implemented yet.")
    input("OK")


def get_subscribed_emails():
    view.print_error_message("Not implemented yet.")
    input("OK")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
