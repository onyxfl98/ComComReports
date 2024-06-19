#!/usr/bin/python3.12

"""Main module of ComComReports app."""

from icecream import install, ic
from get_folder import get_folder

install()


def main():
    """Main function executed when this module is directly run"""

    ic.disable()

    # Get folder path from user
    folder_path = get_folder()

    #combine_text_files(folder_path)


if __name__ == "__main__":
    main()
