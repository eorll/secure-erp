from model.hr import hr
from view import terminal as view


def list_employees():
    lista = hr.read_customers_list()
    view.print_table(lista,hr.HEADERS)


def add_employee():
    new_employee = view.get_inputs(hr.HEADERS[1:]) 
    hr.add_employee(new_employee)
    view.get_input("Employee added. Press enter")


def update_employee():
    view.print_menu("List of employee: ", hr.list_of_employee)
    employee_to_update = view.get_input("number of employee to update: ")
    updated_employee = view.get_inputs(hr.HEADERS[1:]) 
    hr.update_employee(employee_to_update, updated_employee)
    view.get_input("Employee updated. Press enter")


def delete_employee():
    view.print_menu("List of employee: ", hr.list_of_employee)
    employee_to_delete = view.get_input("number of employee to delete: ")
    hr.delete_employee(employee_to_delete)
    view.get_input("Employee deleted. Press enter")


def get_oldest_and_youngest():
    view.print_message(hr.oldest_youngest_employee())
    view.get_input("\nPress enter to continue")


def get_average_age():
    current_year = 2020
    result = hr.employees_average(current_year)
    view.print_message("The average age of employees is: " + str(result))
    view.get_input("\nPress enter to continue")


def next_birthdays():
    given_date = view.get_input("Define the date: (format YYYY-MM-DD, e.g. 2020-04-04)")
    result = hr.employees_birthday(given_date)
    view.print_message("Employees having birthdays within the two weeks: " + str(result))
    view.get_input("\nPress enter to continue")


def count_employees_with_clearance():
    given_clerance = int(view.get_input("Define the minimum clerance: "))
    result = hr.count_employees_clerance(given_clerance)
    view.print_message("Employees with at least the given clearance level: " + str(result))
    view.get_input("\nPress enter to continue")


def count_employees_per_department():
    result = hr.count_employees_department()
    #result = "\n\t".join(result)
    view.print_message("Employees per department: " + str(result))
    view.get_input("\nPress enter to continue")



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
