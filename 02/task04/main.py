def hello() -> str:
    """
    Returns a greeting message.
    """
    return "How can I help you?"

def add_contact(args: list, contacts: dict) -> str:
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

    try:
        name, phone = args

        if name in contacts:
            response = input("Would you like to update the existing contact? [yes/no]")
            if response == 'yes':
                return change_contact(args, contacts)

        contacts[name] = phone
        return "Contact added."
    except ValueError as val_err:
        return f"Error: {str(val_err)}"
    except Exception as ex:
        return f"Unexpected error: {str(ex)}"

def change_contact(args: list, contacts: dict) -> str:
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

    try:
        name, phone = args

        if name not in contacts:
            response = input(f"Contact [{name}] does not exist. Would you like to create a new one? [yes/no]")
            if response == 'yes':
                return add_contact(args, contacts) 
        
        contacts[name] = phone
        return "Contact changed."
    except ValueError as val_err:
        return f"Error: {str(val_err)}"
    except Exception as ex:
        return f"Unexpected error: {str(ex)}"

def show_phone(name: str, contacts: dict) -> str:
    """
    Displays the phone number of a given contact.

    Args:
        name (str): 
            The name of the contact.
        contacts (dict): 
            Dictionary containing all contacts.

    Returns:
        str: The phone number of the contact or an error message.
    """

    if name not in contacts:
        return f"Contact [{name}] does not exist. Please add it first."
    return contacts[name]

def show_all(contacts: dict) -> None:
    """
    Prints all contacts and their phone numbers.

    Args:
        contacts (dict): Dictionary containing all contacts.
    """
    # Calculate minimum number of name's characters wide for alignment.
    pad = max(len(name) for name in contacts.keys())
    [print(f"{name:{pad}} : {phone}") for name, phone in contacts.items()]

def close() -> str:
    """
    Returns a goodbye message when program is closing.

    Returns:
        str: Goodbye message.
    """
    return "Good bye!"

def parse_input(user_input: str) -> tuple:
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
                print(show_phone(*args, contacts))
            elif command == 'all':
                show_all(contacts)
            else:
                print("Invalid command.")
        except Exception as ex:
            print(f"Unexpected error: {str(ex)}")

if __name__ == '__main__':
    main()