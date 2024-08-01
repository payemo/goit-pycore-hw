import os
from functools import wraps
from booklib.entities import *
from typing import Callable, Dict, List, Tuple, Any

def input_error(func: Callable) -> Callable:
    """
    Decorator for handling common input errors.

    Args:
        func (Callable): The function to wrap.

    Returns:
        Callable: The wrapped function with error handling.
    """
    @wraps(func)
    def inner(*args: Any, **kwargs: Any):
        try:
            return func(*args, **kwargs)
        except booklibex.RecordNotFoundException as rnf:
            return str(rnf)
        except (booklibex.InvalidBirthdayException, booklibex.InvalidPhoneNumberException) as e:
            return str(e)
        except IndexError as ie:
            return str(ie)
    return inner

def hello() -> str:
    """
    Returns a greeting message.
    """
    return "How can I help you?"

@input_error
def add_contact(args: List[str], book: AddressBook) -> str:
    """
    Adds a new contact or updates an existing contact.

    Args:
        args (List[str]): List containing the contact name and phone number.
        book (AddressBook): The address book to add the contact to.

    Returns:
        str: Message indicating the result.
    """
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args: List[str], book: AddressBook) -> str:
    """
    Changes an existing contact's phone number.

    Args:
        args (List[str]): List containing the contact name, old phone number, and new phone number.
        book (AddressBook): The address book to update the contact in.

    Returns:
        str: Message indicating the result.
    """
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is not None:
        record.edit_phone(old_phone, new_phone)
        return "Phone changed."
    else:
        record = Record(name)
        record.add_phone(new_phone)
        book.add_record(record)
        return "Contact added."

@input_error
def show_phone(args: List[str], book: AddressBook) -> str:
    """
    Displays the phone number of a given contact.

    Args:
        args (List[str]): List containing the contact name.
        book (AddressBook): The address book to search in.

    Returns:
        str: The phone number(s) of the contact.
    """
    if not args:
        raise IndexError("Argument not found.")
    record = book.find(args[0])
    if record is not None:
        return record.show_phones()
    else:
        raise booklibex.RecordNotFoundException(args[0])

@input_error
def show_all(book: AddressBook) -> None:
    """
    Prints all contacts and their phone numbers.

    Args:
        book (AddressBook): Address book containing information about each user.
    """
    for user_name, user_info in book.items():
        print(f"{user_name:<12} : {user_info.show_phones()}")

@input_error
def add_birthday(args: List[str], book: AddressBook) -> str:
    """
    Adds a birthday to an existing contact.

    Args:
        args (List[str]): List containing the contact name and birthday.
        book (AddressBook): The address book to update.

    Returns:
        str: Message indicating the result.
    """
    name, bday, *_ = args
    user = book.find(name)
    if user is not None:
        user.add_birthday(bday)
        return f"Birthday {bday} for user '{name}' was added."
    else:
        raise booklibex.RecordNotFoundException(name)

@input_error
def show_birthday(args: List[str], book: AddressBook) -> str:
    """
    Displays the birthday of a given contact.

    Args:
        args (List[str]): List containing the contact name.
        book (AddressBook): The address book to search in.

    Returns:
        str: The birthday of the contact.
    """
    name, *_ = args
    user = book.find(name)
    if user is not None:
        return str(user.birthday)
    else:
        raise booklibex.RecordNotFoundException(name)

def birthdays(book: AddressBook) -> None:
    """
    Prints the birthdays of contacts that happens in the next 7 days.

    Args:
        book (AddressBook): The address book containing contacts.
    """
    for birthdays in book.get_upcoming_birthdays():
        print(birthdays)

def close() -> str:
    """
    Returns a goodbye message when program is closing.

    Returns:
        str: Goodbye message.
    """
    return "Good bye!"

def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """
    Parses user input into a command and arguments.

    Args:
        user_input (str): 
            The raw input from the user.

    Returns:
        tuple: The command and its arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main() -> None:
    book = restore_address_book()
    print("Welcome to the assistance bot!")

    while True:
        try:
            user_input = input('"Enter a command: ').strip().lower()
            command, *args = parse_input(user_input)

            if command in ['close', 'exit']:
                print(close())
                break
            elif command == 'hello':
                print(hello())
            elif command == 'add':
                print(add_contact(args, book))
            elif command == 'change':
                print(change_contact(args, book))
            elif command == 'phone':
                print(show_phone(args, book))
            elif command == 'all':
                show_all(book)
            elif command == 'add-birthday':
                print(add_birthday(args, book))
            elif command == 'show-birthday':
                print(show_birthday(args, book))
            elif command == 'birthdays':
                birthdays(book)
            else:
                print("Invalid command.")
        except Exception as ex:
            print(f"Unexpected error: {str(ex)}")

    save_address_book(book)

def restore_address_book(filename="addressbook.pkl") -> AddressBook:
    """Restores the address book information from file.
    
    Args:
        filename (str): The name of the file from which data should be restored.

    Returns:
        (AddressBook): deserialized (restored) address book with a state a previously closed session.
    """
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def save_address_book(book: AddressBook, filename="addressbook.pkl") -> None:
    """Saves the address book in binary format into the file.
    
    Args:
        book (AddressBook): object of the address book to be saved.
        filename (str): name of the output file.
    """
    with open(filename, "wb") as f:
        pickle.dump(book, f)

if __name__ == '__main__':
    main()