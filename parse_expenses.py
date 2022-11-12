import datetime

def parse_expenses(expenses):
    """
    Parse expenses from a string into a list of tuples (category, value).
    Ignore lines starting with #.
    Parse the date using datetime.
    Example expenses_string:
        Groceries -34.01
        Food 2.59
        Netflix -8.72
    """
    