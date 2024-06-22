#!/usr/bin/python3.12

"""
This module will determine and return the report date

In it's first instance it will just ask for the month and year.

Eventually it should receive info to parse it from the chosen input files and folder
"""

from datetime import date


def get_report_date() -> tuple:
    """Ask the user for the report date"""

    date_valid = False

    while not date_valid:
        # Loop until a "valid" year and month are entered.

        raw_year = input("Enter the report year: ")  # Later default to current year

        raw_month = input(
            "Enter report month as a number: "
        )  # Later default to month previous

        # very basic sanity check. Should eventually be more thorough
        if int(raw_year) <= date.today().year and int(raw_year) >= (
            date.today().year - 10
        ):
            validated_year = int(raw_year)
            print("Validated year.")

            if int(raw_month) >= 1 and int(raw_month) <= 12:
                validated_month = int(raw_month)
                print("validated Month")

                date_valid = True

        else:
            date_valid = False

    return (validated_year, validated_month)


def main():
    """Main function executed when this module is directly run"""


if __name__ == "__main__":
    main()
