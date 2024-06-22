#!/usr/bin/python3.12

"""Combine reports into a single list"""

import os
import magic

# Main function to process files
def combine_text_files(folder, output_filename="combined.txt") -> list :
    """Aggregates text files into a list"""

    combined_text = []
    # Loop through files in the folder
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder, filename)

            # Detect text file encoding
            blob = open(file_path, 'rb').read()
            m = magic.Magic(mime_encoding=True)
            file_encoding = m.from_buffer(blob)

            # Read the content of the text file
            with open(file_path, "r", encoding=file_encoding) as file:
                content = file.read()
                # Add content with(out) a separator (optional)
                combined_text.append(
                    content #+ "\n"
                )
    return combined_text

def main():
    """Main function executed when this module is directly run"""

if __name__ == "__main__":
    main()
