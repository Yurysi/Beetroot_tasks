"""
Task 2

Extend Phonebook application

Functionality of Phonebook application:

    Add new entries
    Search by first name
    Search by last name
    Search by full name
    Search by telephone number
    Search by city or state
    Delete a record for a given telephone number
    Update a record for a given telephone number
    An option to exit the program


The first argument to the application should be the name of the phonebook.
Application should load JSON data, if it is present in the folder with
application, else raise an error. After the user exits, all data should be
saved to loaded JSON.
"""
import json

FILE_NAME = "phonebook.json"


def save_to_disk(phone_book: dict, file_name: str) -> None:
    """
    :param phone_book: dict object
    :param file_name: str file_name. Example: phonebook.json
    :return: None
    """

    with open(file_name, 'w') as file:
        json.dump(phone_book, file)


def read_from_file(path_to_file: str):
    """
    :param path_to_file: str
    :return: dict
    """
    try:
        with open(path_to_file, "r", encoding="utf-8") as book:
            temp = json.load(book)
    except:
        print("There is no such file on that path!")
        return None
    return temp


def add_item(my_book: dict):
    first_name = input("Enter your first_name: ")
    last_name = input("Enter your last_name: ")
    full_name = input("Enter your full_name: ")
    phone_number = input("phone_number: ")
    city = input("Enter your city or state: ")
    my_book[phone_number] = {'first_name': first_name, 'last_name': last_name,
                             'full_name': full_name,
                             'phone_number': phone_number,
                             'city': city}
    return my_book


def delete_item(my_book: dict):
    phon_num = input("Enter phone number: ")
    try:
        my_book.pop(phon_num)
    except KeyError:
        print("Incorekt phone number")
        return None


def search_first_name(my_book):
    try:
        search_first = input("Please, write first name: ")
        for items in my_book:
            if my_book[items]['first_name'] == search_first:
                print(my_book[items])
            else:
                print("Your name does not exist!")
    except KeyError:
        print("Your name does not exist!")


def search_last_name(my_book):
    try:
        search_last = input("Please, write first name: ")
        for items in my_book:
            if my_book[items]['last_name'] == search_last:
                print(my_book[items])
            else:
                print("Your name does not exist!")
    except (TypeError, KeyError):
        print("Your name does not exist!")


def search_full_name(my_book):
    try:
        search_full_n = input("Please, write first name: ")
        for items in my_book:
            if my_book[items]['full_name'] == search_full_n:
                print(my_book[items])
            else:
                print("Your name does not exist!")
    except (TypeError, KeyError):
        print("Your name does not exist!")


def search_phone_number(my_book):
    try:
        search_phone = input("Please, write your number: ")
        print(my_book[search_phone])
    except KeyError:
        print("Your phone does not exist!")


def search_City(my_book):
    try:
        search_city = input("Please, write first name: ")
        for items in my_book:
            if my_book[items]['city'] == search_city:
                print(my_book[items])
            else:
                print("Your name does not exist!")
    except (TypeError, KeyError):
        print("Your name does not exist!")


def update_item(my_book: dict):
    phone_number = input("Please, write your phone number: ")
    new_phone_number = input("Please, write a new phone number: ")
    new_first_name = input('Please, write  a new first name: ')
    new_last_name = input('Please, write  a new last name: ')
    new_full_name = input('Please, write  a new last name: ')
    new_city = input('Please, write  a new city: ')
    my_book[phone_number]['phone_number'] = new_phone_number

    if new_city:
        my_book[phone_number]['city'] = new_city
    if new_first_name:
        my_book[phone_number]['first_name'] = new_first_name
    if new_last_name:
        my_book[phone_number]['last_name'] = new_last_name
    if new_last_name:
        my_book[phone_number]['last_name'] = new_last_name
    if new_full_name:
        my_book[phone_number]['last_name'] = new_full_name
    my_book[new_phone_number] = my_book[phone_number]
    del my_book[phone_number]
    return my_book


if __name__ == '__main__':
    data = read_from_file(FILE_NAME)
    if data is None:
        data = {}
    while True:
        choice = input("""
        1 Add new entries 
        2 Search by first name 
        3 Search by last name 
        4 Search by full name
        5 Search by telephone number
        6 Search by city or state
        7 Delete a record for a given telephone number
        8 Update a record for a given telephone number
        9 Look what we have
        10 Exit!\n""")
        if choice == '1':
            add_item(data)
        elif choice == '2':
            search_first_name(data)
        elif choice == '3':
            search_last_name(data)
        elif choice == '4':
            search_full_name(data)
        elif choice == '5':
            search_phone_number(data)
        elif choice == '6':
            search_City(data)
        elif choice == '7':
            delete_item(data)
        elif choice == '8':
            update_item(data)
        elif choice == '9':
            print(data)
        if choice == '10':
            save_to_disk(data, FILE_NAME)
            break
