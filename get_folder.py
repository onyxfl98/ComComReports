#!/usr/bin/python3.12

"""Select folder containing reports"""

from pathlib import Path

def get_folder() -> str:
    """Ask the user for a directory and validate"""

    #Future - browse

    user_folder_name = input("Enter folder name for report files: ")

    path_folder = Path(user_folder_name)

    ic(path_folder)

    if path_folder.exists() and path_folder.is_dir():
        print(str(path_folder) + " is a valid folder")
        print(str(list(path_folder.glob('*.txt'))))

        return str(path_folder)
    
    else:
        print(str(path_folder) + " isn't a valid folder")
        return ""


def main():
    """Main function executed when this module is directly run"""

if __name__ == "__main__":
    main()
