# My birthday is October 6, 2004

def days_since_birthday(birthday):
    """
    Calculates the number of days that have passed since the birth year and the current year are excluded

    :param birthday: The birthdate as a string in "DD-MM-YYYY" format.
    :return: The total number of days excluding the birth year and current year.
    """
    # Extract birth year from the string
    birth_year = int(birthday.split("-")[-1])

    # get the current year
    current_year = 2025  # Assuming current year is 2025

    # Calculate the total number of whole years in between
    whole_years = current_year - birth_year - 1

    # Each year has 365 days (ignoring leap years as per class materials)
    days_passed = whole_years * 365

    return days_passed

print(days_since_birthday("06-10-2004"))

#7300 days have passed
