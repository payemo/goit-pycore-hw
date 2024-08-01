class InvalidPhoneNumberException(ValueError):
    """
    Exception raised for invalid phone numbers.

    Attributes:
        phone -- input phone number which caused the error
    """
    def __init__(self, phone: str) -> None:
        super().__init__(f"Invalide phone number: {phone}")

class InvalidBirthdayException(ValueError):
    """
    Exception raised for invalid birthday format.

    Attributes:
        birthday -- input birthday which caused the error
        format -- expected format of the birthday
    """
    def __init__(self, birthday: str, format: str) -> None:
        super().__init__(f"Invalid date: {birthday}. Use '{format}' format.")

class RecordNotFoundException(Exception):
    """
    Exception raised when a contact record is not found.

    Attributes:
        name -- name of the contact which was not found
    """
    def __init__(self, name: str) -> None:
        super().__init__(f"Contact not found: '{name}'.")