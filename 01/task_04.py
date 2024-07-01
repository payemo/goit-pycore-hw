from datetime import datetime, timedelta

BDAY_FORMAT = "%Y.%m.%d"

def get_upcoming_birthdays(users: list[dict[str, str]])->list[dict[str, str]]:
    """Determines whose birthday are 7 days ahead including the current day.
    If birthday falls on a weekend, the greeting moves to the following Monday.

    User's birthday date is always specified in the format: '%Y.%m.%d'
    
    Parameters:
        users: List of dictionaries containing user data with keys 'name' and 'birthday'.

    Returns:
        List of dictionaries with keys 'name' and 'congratulation_date' in '%Y.%m.%d' format.
    """

    today = datetime.now().date()
    end_date = today + timedelta(days=7)

    greetings = []

    for user in users:
        name, bday = user.values()
        # Convert user's bday into datetime object.
        user_bday = datetime.strptime(bday, BDAY_FORMAT).date()

        # Set the birthday to the current year
        bday_this_year = user_bday.replace(year=today.year)

        if today <= bday_this_year <= end_date:
            if bday_this_year.weekday() == 5: # Saturday
                bday_this_year += timedelta(days=2)
            elif bday_this_year.weekday() == 6: # Sunday
                bday_this_year += timedelta(days=1)
            
            greetings.append({'name': name, 'congratulation_date': bday_this_year.strftime(BDAY_FORMAT)})

    return greetings

users = [
    {"name": "John Doe", "birthday": "1985.07.01"},
    {"name": "Jane Smith", "birthday": "1990.07.07"},
    {"name": "Jane Smith X", "birthday": "1990.07.06"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)