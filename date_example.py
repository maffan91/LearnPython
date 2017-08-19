given_year = 2017
given_date = 28
given_month = 2

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]
date_range = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']


def validate_date(date, month, year):
    if date < 1 or date > 31:
        return False
    elif month < 1 or month > 12:
        return False
    elif 28 < date < 30 and month == 2 and year % 4 != 0:
        return False
    elif date == 31 and month in [4, 6, 9, 11] or date > 29 and month == 2:
        return False
    else:
        return True


if validate_date(given_date, given_month, given_year):
    print(str(given_date) + date_range[given_date - 1] + ' ' + months[given_month - 1] + ',' + str(given_year))
else:
    print("Invalid date")
