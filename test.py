#!/usr/bin/python3.12

"""Used as the main module for testing purposes"""

from get_folder import get_folder
from icecream import install, ic

install()


def main():
    """Main function executed when this module is directly run"""

    report_folder = get_folder()
    ic(report_folder)

    

if __name__ == "__main__":
    main()
