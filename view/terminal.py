import os

def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(f'{title}')
    n = 0
    for option in list_options:
        print(f"({n}) {option}")
        n += 1


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """

    if type(result) is float or type(result) is int:
        print(f"{label}: {round(result, 2)}")

    if type(result) is list or type(result) is tuple:
        print(f'{label}: ')
        for item in result:
            print(f'{item}')

    if type(result) is dict:
        print(f'{label}: ')
        for key,value in result.items():
            print(f'{key}: {value}')


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table, labels):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    # dodaje nagłówki do tabeli
    row = ''
    bar = ''
    for i in labels:
        row += f'|{i:^20}'
    row += ' |'
    for x in range(len(row)):
        bar += '-'
    print(bar)
    print(row)

    # drukuje tabele
    for i in table:
        row = ''
        bar = ''
        for j in i:
            row += f'|{j:^20}'
        row += ' |'
        for x in range(len(row)):
            bar += '-'
        print(bar)
        print(row)
    print(bar)
        
# print_table([['Jajko',2,3,4,5],[2,2,2245,4,5]])


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    user_input = input(f"Enter {label} ") 
    os.system('cls')
    return user_input


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    print("CURRENT LABELS:")
    inputs_list = []
    for label in labels:
        new_item = input(f'Enter {label}: ')
        inputs_list.append(new_item)
    os.system('cls')
    return inputs_list


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(f'Error! {message}')
