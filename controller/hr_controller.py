from model.hr import hr
from view import terminal as view


def list_employees():
    lista = hr.read_customers_list()
    view.print_table(lista)
    input("OK")


def add_employee():
    view.print_error_message("Not implemented yet.")


def update_employee():
    view.print_error_message("Not implemented yet.")


def delete_employee():
    view.print_error_message("Not implemented yet.")


def get_oldest_and_youngest():
    view.print_error_message("Not implemented yet.")


def get_average_age():
    view.print_error_message("Not implemented yet.")


def next_birthdays():
    given_date = view.get_input("Define the date: (format YYYY-MM-DD, fe. 2020-04-04)")
    result = hr.employees_birthday(given_date)
    view.print_message("Employees having birthdays within the two weeks: \n\t" + str(result))
    input("OK")


def count_employees_with_clearance():
    given_clerance = int(view.get_input("Define the minimum clerance: "))
    result = hr.count_employees_clerance(given_clerance)
    view.print_message("Employees with at least the given clearance level: \n\t" + str(result))
    input("OK")


def count_employees_per_department():
    result = hr.count_employees_department()
    view.print_message("Employees per department: \n\t" + str(result))
    input("OK")



def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
