from model.crm import crm
from view import terminal as view


def list_customers():
    customer_list = crm.read_customers_list()
    view.print_table(customer_list,crm.HEADERS)


def add_customer():
    customer_to_add = view.get_inputs(crm.HEADERS[1:]) #pobieranie danych od użytkownika
    crm.new_customer(customer_to_add)
    view.get_input("\nCustomer added. Press enter")


def update_customer():
    list_customers()
    number_of_line = int(view.get_input("Chose row to update"))
    view.print_message("You want to update line number " + str(number_of_line))
    customer_list = crm.read_customers_list()
    #view.print_table(customer_list[number_of_line-1],crm.HEADERS)
    view.print_message(customer_list[number_of_line-1])
    customer_to_update = view.get_inputs(crm.HEADERS[1:]) #pobieranie danych od użytkownika
    crm.new_customer(customer_to_update,option=number_of_line)
    view.get_input("\nCustomer updated. Press enter")


def delete_customer():
    list_customers()
    number_of_line = int(view.get_input("Chose row to remove"))
    view.print_message("You want to remove line number " + str(number_of_line))
    customer_list = crm.read_customers_list()
    #view.print_table(customer_list[number_of_line-1],crm.HEADERS)
    view.print_message(customer_list[number_of_line-1])
    customer_to_remove = -int(number_of_line)
    crm.new_customer([""],option=customer_to_remove)
    view.get_input("\nCustomer deleted. Press enter")


def get_subscribed_emails():
    emails = crm.get_emails()
    emails = "\n\t".join(emails)
    view.print_message("Subscriber e-mails: \n\t" + emails)
    view.get_input("\nPress enter to continue")


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
