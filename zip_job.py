import os
import zipfile
from pathlib import Path




# Constants
ELEMENTS = ['a', 'b', 'c', 'd']
VERSION = os.getenv('VERSION', '1.2.0')




def create_text_file(filename):
    """Create a text file with a predefined content."""
    content = f"This is the content of {filename}"
    Path(filename).write_text(content)




def create_zip_file(zip_name, filename):
    """Create a zip file containing the specified file."""
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        zipf.write(filename)




def file_exists(file_path):
    """Check if a file exists."""
    return Path(file_path).is_file()




def main():
    for element in ELEMENTS:
        txt_filename = f'{element}.txt'
        zip_filename = f'{element}_{VERSION}.zip'




        create_text_file(txt_filename)




        if not file_exists(txt_filename):
            raise FileNotFoundError(f"Text file {txt_filename} not found.")




        create_zip_file(zip_filename, txt_filename)




        if not file_exists(zip_filename):
            raise FileNotFoundError(f"Zip file {zip_filename} not found.")




if __name__ == "__main__":
    main()
