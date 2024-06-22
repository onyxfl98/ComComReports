#!/usr/bin/python3.12

"""Main module of ComComReports app."""

from icecream import install, ic
from get_folder import get_folder
from combine_files import combine_text_files

install()


def main():
    """Main function executed when this module is directly run"""

    ic.disable()

    # Get folder path from user
    inbound_folder_path = get_folder()

    outbound_file = "/home/onyx/ReportsTest/combined_files.txt"

    contents_list = combine_text_files(inbound_folder_path,outbound_file)


if __name__ == "__main__":
    main()
