from datetime import datetime, date

# More about documentation style: https://developer.lsst.io/v/DM-5063/docs/py_docs.html#

def get_days_from_today(date_str: str)->int:
    r"""Returns the difference between input and current dates.
    
    Parameters
    ----------
    date_str : str
        Date represented in 'YYYY-MM-dd' format.
    
    Returns
    -------
    days : int
        Amount of days between current and input dates.

    Raises
    ------
    ValueError
        Can't parse input date string into datetime object. 
    """

    try:
        now = date.today()
        # Create date time object from it's string representation.
        dt = datetime.strptime(date_str, "%Y-%m-%d").date()
        # Get time delta and return the absolute value in days.
        dt_diff = abs(now - dt)
        return dt_diff.days
    except ValueError as e:
        print(e)

#print(get_days_from_today("2029-10-09"))
print(get_days_from_today("2024-08-25"))