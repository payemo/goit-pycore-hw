from datetime import datetime, timedelta

BDAY_FORMAT = "%Y.%m.%d"

def get_upcoming_birthdays(users: list[dict[str, str]])->list[dict[str, str]]:
    """Determines whose birthday are 7 days ahead including the current day.
    If birthday falls on a weekend, the greeting moves to the following Monday.

    User's birthday date is always specified in the following format: '%Y.%m.%d'
    
    Parameters:
        users: list of data about organization's users.

    Returns:
        List of users whose birthday are 7 days ahead or users whose birthday
        falls on the weekend.
    """

    today = datetime.now().today()

    greetings = []

    for user in users:
        name, bday = user.values()
        # Convert user's bday into datetime object.
        user_bday = datetime.strptime(bday, BDAY_FORMAT).date()

        bday_this_year = datetime(today.year, user_bday.month, user_bday.day)

        if bday_this_year >= today:
            next_bday = datetime(today.year, user_bday.month, user_bday.day)

            # Check if user's bday happens in a weekend.
            if next_bday.weekday() >= 5:
                # Get offset to get the beginning of the next weekend.
                day_offset = 7 - next_bday.weekday()
                greet_day = next_bday + timedelta(days=day_offset)
            else:
                greet_day = next_bday
            
            greetings.append({'name': name, 'congratulation_date': greet_day.strftime(BDAY_FORMAT)})

    return greetings

users = [
    {"name": "John Doe", "birthday": "1985.07.01"},
    {"name": "Jane Smith", "birthday": "1990.07.07"},
    {"name": "Jane Smith X", "birthday": "1990.07.06"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)