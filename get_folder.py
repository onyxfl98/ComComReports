#!/usr/bin/python3.12

"""Select folder containing reports"""

from tkinter import filedialog, Tk

def get_folder() -> str:
    """Ask the user for a directory and validate"""

    root = Tk()
    root.withdraw()  # Hide the main window

    folder_selected = ()

    while not isinstance(folder_selected, str):
        folder_selected = filedialog.askdirectory(title="Please select folder")

        ic(folder_selected)

        if not isinstance(folder_selected, str):
            print("Selection cancelled please try again")

    return folder_selected

def main():
    """Main function executed when this module is directly run"""

if __name__ == "__main__":
    main()
