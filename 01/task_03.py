import re

def normalize_phone(phone_number:str)->str:
    r"""Normalizes the input phone number to the format +38XXXXXXXXX.

    Papameters
    ----------
    phone_number
        Input phone number in various formats.

    Returns
    -------
    normalized_phone_number
        Normalized phone number in the format +38XXXXXXXXX.

    Raises
    ------
    ValueError
        If the input phone number doesn't match the expected pattern.

    """

    # Remove all non-digit characters except '+' if it exists at the beginning
    phone_number = re.sub(r"[^+?\d]", "", phone_number)

    # VARIAN 1.
    # if phone_number.startswith('+'):
    #     # If it starts with '+', ensure it follows the pattern +38XXXXXXXXX
    #     if not re.match(r"^\+380\d{9}$"):
    #         raise ValueError(f"{phone_number} is invalid.")
    # else:
    #     if re.match(r"^380\d{9}$"): # Check for 380XXXXXXXXXX
    #         phone_number = '+' + phone_number
    #     elif re.match(r"^\d{10}$"): # Check for 0XXXXXXXXX
    #         phone_number = '+38' + phone_number
    #     else:
    #         raise ValueError(f"{phone_number} is invalid.")

    # VARIANT 2
    # Check if number starts with `+38` or `38` or `+` followed by exactly 10 digits.
    if not re.match(r"^(?:\+|\+38|38)?\d{10}$", phone_number):
        raise ValueError(f"{phone_number} is invalid.")
    
    if phone_number.startswith('38'):
        phone_number = '+' + phone_number
    elif not phone_number.startswith('+'):
        phone_number = '+38' + phone_number
    
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
    #"38050 111 22 1   ", # Error value
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)