import random
import string
import itertools  

def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    
    small_letters = list(string.ascii_lowercase)
    capital_letters = list(string.ascii_uppercase)
    digits = list(string.digits)
    special_chars = list(allowed_special_chars)

    list_of_lists = [small_letters, capital_letters, digits, special_chars]
    list_of_allowed_numbers = [number_of_small_letters, number_of_capital_letters, number_of_digits, number_of_special_chars]

    new_id_list = []

    for (i,j) in zip(list_of_lists, list_of_allowed_numbers):
        for k in range(j):
            new_id_list.append(random.choice(i))
    
    random.shuffle(new_id_list)
    new_id = ''.join(new_id_list)
    return new_id
