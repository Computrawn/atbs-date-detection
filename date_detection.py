# python3
# dateDetection.py — A program that uses regex to determine valid dates based on DD/MM/YYYY format.

"""
Made ready for hub. Needs refactor.
"""

import re, pyperclip


def dateValidator(userInput):
    dateRegex = re.compile(r"(\d{2})/(\d{2})/(\d{4})", re.DOTALL)

    mo = dateRegex.findall(userInput)

    for date in range(len(mo)):
        day, month, year = mo[date]
        day = int(day)
        month = int(month)
        year = int(year)
        if month > 12 or day > 31 or year < 1000 or year >= 3000:
            pass
        elif month == 2:
            if day == 29 and year % 4 == 0:
                if year % 100 == 0 and year % 400 != 0:
                    pass
                else:
                    print(f"{day:02}/{month:02}/{year}")
            elif day > 28:
                pass
            else:
                print(f"{day:02}/{month:02}/{year}")
        elif month == 4 or 6 or 9 or 11 and day > 30:
            if day > 30:
                pass
            else:
                print(f"{day:02}/{month:02}/{year}")


# userInput = input('Enter text here: ')    # manual input argument.
userInput = str(pyperclip.paste())  # pasteboard input argument using pyperclip module.
# Make a userInput that looks for a file in current working directory and user defined path.


dateValidator(userInput)
