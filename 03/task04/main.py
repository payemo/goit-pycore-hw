from functools import wraps
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
        except ValueError:
            return "Give me name a phone please."
        except KeyError:
            return "Specified name does not exist."
        except IndexError:
            return "Enter the name."
    return inner

def hello() -> str:
    """
    Returns a greeting message.
    """
    return "How can I help you?"

@input_error
def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Adds a new contact or updates an existing contact if the user confirms it.

    Args:
        args (list):
            List containing the name and phone number.
        contacts (dict):
            Dictionary containing all contacts.

    Returns:
        str: Status message indicating the result.
    """

    name, phone = args

    if name in contacts:
        response = input("Would you like to update the existing contact? [yes/no]: ").strip().lower()
        if response == 'yes':
            return change_contact(args, contacts)

    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Changes an existing contact or prompts to create a new one if it doesn't exist.

    Args:
        args (list):
            List containing the name and phone number.
        contacts (dict):
            Dictionary containing all contacts.

    Returns:
        str: Status message indicating the result.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact changed."

@input_error
def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Displays the phone number of a given contact.

    Args:
        args (List[str]): 
            List containing the name of the contact.
        contacts (dict): 
            Dictionary containing all contacts.

    Returns:
        str: The phone number of the contact or an error message.
    """
    if not args:
        raise IndexError
    return contacts[args[0]]

@input_error
def show_all(contacts: Dict[str, str]) -> None:
    """
    Prints all contacts and their phone numbers.

    Args:
        contacts (dict): Dictionary containing all contacts.
    """
    # Calculate minimum number of name's characters wide for alignment.
    pad = max(len(name) for name in contacts.keys())
    for name, phone in contacts.items():
        print(f"{name:{pad}} : {phone}")

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
    print("Welcome to the assistance bot!")

    contacts = {}

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
                print(add_contact(args, contacts))
            elif command == 'change':
                print(change_contact(args, contacts))
            elif command == 'phone':
                print(show_phone(args, contacts))
            elif command == 'all':
                show_all(contacts)
            else:
                print("Invalid command.")
        except Exception as ex:
            print(f"Unexpected error: {str(ex)}")

if __name__ == '__main__':
    main()