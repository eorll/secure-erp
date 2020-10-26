from model.hr import hr
from view import terminal as view


def list_employees(employees):
    employees = hr.get_employees()
    view.print_table(employees)


#for index, list_of_employees in enumerate(list_of_employees, start = 1):
    
#       print(index,list_of_employees)
        
    view.print_error_message("Not implemented yet.")
    
   #not ready yet :)
    

def add_employee(add_emploees, new_employee):
    add_emloyees = view.get_change_input("Please, enter data of the employee you want to add:")
    new_employee = hr.get_employees(add_employees)
    view.print.message("Addinig employee:")
    view.print_table(new_employee)
    view.get_input("Please, enter data of the employee you want to add:")
    view.print_error_message("Not implemented yet.")


def update_employee(empl_id, employee):
    empl_id = view.get_employee_input("Please, type which employee you wish to update:")
    employee = hr.get_employees(empl_id)
    view.print_message("Updating employee:")
    view.print_table(employee)
    view.get_input("Please type which employee you wish to update:")
    
    
    view.print_error_message("Not implemented yet.")


def delete_employee(delete_employees, deleted_employee):
    delete_employees = view.get_input("Please, enter data of an employee to delete ")
    deleted_employee = hr.get_employees(delete_employees)
    view.print_message("Deleting employee:")
    view.print_table(deleted_employee)
    view.get_input("Please, enter data of an employee to delete ")
    view.print_error_message("Not implemented yet.")
    view.print_error_message("Not implemented yet.")


def get_oldest_and_youngest():
    view.print_error_message("Not implemented yet.")


def get_average_age():
    view.print_error_message("Not implemented yet.")


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    view.print_error_message("Not implemented yet.")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


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
