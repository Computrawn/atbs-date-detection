#!/usr/bin/env python3
# dateDetection.py — An exercise in understanding regular expressions.
# For more information, see README.md.

import re
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.

text_block = """
The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021. 31/06/2100. 
(01/01/2100.)
32/01/1234 ain't even real, man.
02/13/1000*(^
01/01/3214—
**&&^02/02/1988
Write a function 29/02/1800 that uses regular expressions 29/02/2004 to make sure the password string it is passed is strong. A strong password is defined as 29/02/2000 one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least 29/02/1900 one digit. You may 29/02/2500 need to test the 29/02/2500 string against multiple 30/04/2001 regex patterns to validate its strength 31/04/2001.
"""


def main():
    matches = create_regex(text_block)
    valid_dates = vali_date(matches)
    print("The following valid dates were found:")
    for date in valid_dates:
        print(f"— {date}")


def create_regex(user_input):
    date_regex = re.compile(r"(\d{2})/(\d{2})/(\d{4})")
    match_obj = date_regex.findall(user_input)
    return match_obj


def vali_date(matches):
    matching_dates = []
    for index, _ in enumerate(matches):
        day, month, year = matches[index]
        day, month, year = int(day), int(month), int(year)
        if month > 12 or day > 31 or year < 1000 or year >= 3000:
            pass
        elif month == 2:
            if day == 29 and year % 4 == 0:
                if year % 100 == 0 and year % 400 != 0:
                    pass
                else:
                    matching_dates.append(f"{day:02}/{month:02}/{year}")
            elif day > 28:
                pass
            else:
                matching_dates.append(f"{day:02}/{month:02}/{year}")
        elif month == 4 or 6 or 9 or 11 and day > 30:
            if day > 30:
                pass
            else:
                matching_dates.append(f"{day:02}/{month:02}/{year}")
    return matching_dates


if __name__ == "__main__":
    main()
