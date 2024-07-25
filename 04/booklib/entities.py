import re
from collections import UserDict

class Field:
    """
    Base class for different fields.
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    """
    Class for storing names.
    """
    pass

class Phone(Field):
    """
    Class for storing phone numbers. Validates that the number has 10 digits.
    """
    def __init__(self, value):
        if not re.match(r"^\d{10}$", value):
            # May be implement custom exception
            raise ValueError(f"Invalide phone number: {value}")
        super().__init__(value)

class Record:
    """
    Class for storing a contact record, including a name and multiple phone numbers.
    """
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str) -> Phone:
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        phone = self.find_phone(old_phone)
        if phone:
            phone.value = new_phone

    def find_phone(self, phone: str) -> Phone:
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self) -> str:
        return f"{self.name.value}, phones: {';'.join(str(p) for p in self.phones)}"
    
class AddressBook(UserDict):
    """
    Class for storing a collection of records, indexed by name.
    """
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data.get(name)

    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]
