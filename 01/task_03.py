import re

REPLACEMENT_PATTERN = r"(?<=[+380])\d{9}}"
REDUNDANT_SYMBOLS = r"\D"

def normalize_phone(phone_number:str)->str:
    r"""Normalizing input phone number and returns the formatted variant.

    Preceding international number always defined and has the following format: '+380'.
    All symbols except '+' that is a part of an international number will be removed.

    Papameters
    ----------
    phone_number : str
        Input phone number.

    Returns
    -------
    normalized_phone_number : str
        Phone number with the following format: +380\d{9}
    """

    # Remove all non digit characters except '+' (if such exists)
    phone_number = re.sub(r"[^+?\d]", "", phone_number)

    if not re.match(r"^(?:\+|\+38|38)?\d{10}$", phone_number):
        # The phone number may start with: '+38' or '38' or '+',
        # so there must be exact 10 digits not counting the prefix.
        raise ValueError(f"{phone_number} is invalid.")
    else:
        if not phone_number.startswith('+'):
            # Prepending phone number with an appropriate prefix code: '+' | '+38'
            prefix = '+38' if not phone_number.startswith('38') else '+'
            phone_number = prefix + phone_number
    
    return phone_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    #"38050 111 22 1   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)