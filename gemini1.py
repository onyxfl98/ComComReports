import os
from tkinter import filedialog, Tk

# Function to get the folder path from user selection
def get_folder_path():
  root = Tk()
  root.withdraw()  # Hide the main window
  folder_selected = filedialog.askdirectory(title="Select Folder")
  return folder_selected

# Main function to process files
def combine_text_files(folder_path, output_filename="combined.txt"):
  combined_text = ""
  # Loop through files in the folder
  for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
      file_path = os.path.join(folder_path, filename)
      # Read the content of the text file
      with open(file_path, "r") as file:
        content = file.read()
        # Add content with a separator (optional)
        combined_text += content + "\n\n"  # Add newline separators between files

  # Write the combined text to a new file
  with open(os.path.join(folder_path, output_filename), "w") as output_file:
    output_file.write(combined_text)
  print(f"Successfully combined text files into '{output_filename}'")

# Get folder path from user
folder_path = get_folder_path()

# Check if folder is valid
if folder_path:
  combine_text_files(folder_path)
else:
  print("No folder selected.")
