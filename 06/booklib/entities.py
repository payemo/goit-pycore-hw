import re
import pickle
import copy
import booklib.exceptions as booklibex
from datetime import datetime, timedelta
from collections import UserDict

BDAY_FORMAT = "%d.%m.%Y"

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
    Class for storing phone numbers. V
    lidates that the number has 10 digits.
    """
    def __init__(self, value):
        if not re.match(r"^\d{10}$", value):
            raise booklibex.InvalidPhoneNumberException(value)
        super().__init__(value)

class Birthday(Field):
    """
    Class for storing birthdays in the correct format.
    """
    def __init__(self, value: str):
        if not re.match(r"(^0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4}$)", value):
            raise booklibex.InvalidBirthdayException(value, BDAY_FORMAT)
        super().__init__(datetime.strptime(value, BDAY_FORMAT).date())

class Record:
    """
    Class for storing a contact record, including a name and multiple phone numbers.
    """
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def show_phones(self, delim=";") -> str:
        """
        Show all phone numbers of the contact separated by a delimiter.
        """
        if self.phones:
            return delim.join(str(phone) for phone in self.phones)
        return ""

    def add_phone(self, phone: str) -> Phone:
        """
        Add a phone number to the contact.
        """
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        """
        Remove a phone number from the contact.
        """
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """
        Edit a phone number of the contact.
        """
        phone_info = self.find_phone(old_phone)
        if phone_info is not None:
            index, _ = phone_info
            self.phones[index] = Phone(new_phone)

    def find_phone(self, phone: str) -> tuple[int, Phone]:
        """
        Find a phone number in the contact's phone list.
        """
        for i, p in enumerate(self.phones):
            if p.value == phone:
                return (i, p)
        return None
    
    def add_birthday(self, birthday: str) -> None:
        """
        Set the contact's birthday.
        """
        self.birthday = Birthday(birthday)

    def __str__(self) -> str:
        return f"{self.name.value}, phones: {';'.join(str(p) for p in self.phones)}"
    
class AddressBook(UserDict):
    """
    Class for storing a collection of records, indexed by name.
    """
    def add_record(self, record: Record) -> None:
        """
        Add a new record to the address book.
        """
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        """
        Find a record by name.
        """
        return self.data.get(name)

    def delete(self, name: str) -> None:
        """
        Delete a record by name.
        """
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self)->list[dict[str, str]]:
        """
        Get a list of records with birthdays in the next 7 days.

        Returns:
            List of dictionaries with keys 'name' and 'congratulation_date' in '%d.%m.%Y' format.
        """
        today = datetime.now().date()
        end_date = today + timedelta(days=7)

        greetings = []

        for user_name, record in self.data.items():
            # If birthday field is not specified then skip that user.
            if record.birthday is None:
                continue

            user_bday = record.birthday.value
            bday_this_year = user_bday.replace(year=today.year)

            if today <= bday_this_year <= end_date:
                if bday_this_year.weekday() == 5: # Saturday
                    bday_this_year += timedelta(days=2)
                elif bday_this_year.weekday() == 6: # Sunday
                    bday_this_year += timedelta(days=1)
                
                greetings.append({'name': user_name, 'congratulation_date': bday_this_year.strftime(BDAY_FORMAT)})

        return greetings