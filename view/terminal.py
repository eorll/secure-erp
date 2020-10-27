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
    print("TITLE: ",title , "\nOPTIONS: ")# , list_options, "\n") #
    for i in range(len(list_options)):
        print("\t",i, list_options[i])
    print("\n")


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print("MESSAGE:" ,  message, "\n")


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    #print(table)
    counter = 1
    for i in table:
        row = ''
        bar = ''
        for j in i:
            row += f'|{j:^5}'
        row += ' |'
        for x in range(len(row)):
            bar += '-'
        print(bar)
        print(counter,row)
        counter+=1
    print(bar)
        
#print_table([['Jajko',2,3,4,5],[2,2,2245,4,5]])


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """

    label = "".join(label)
    print("Current label:"  + label + "\n")
    print("USER ACTION| Enter number of label:")
    user_input = input(" ") ##
    return user_input

#label = ["Pierwsza Linia 123 2"]
#get_input(label)


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """

    new_line = []
    
    for i in range(1,len(labels)):
        user_input = input("USER ACTION| Enter "+ labels[i]+ " for new user: ")
        new_line.append(user_input)

    return new_line

#labels = [["Pierwsza Linia 123 2"], ["Druga linia 122 2"]]
#get_inputs(labels)

def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print("ERROR MESSAGE:" ,  message, "\n")