def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except (FileNotFoundError, IOError) as e:
        raise e

def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
    except IOError as e:
        raise e

def create_modified_filename(original_filename):
    return "modified_" + original_filename

file_name = input("Enter the file name/file path: ")

try:
    content = read_file(file_name)
    print("Original Content:", content)
    
    new_file_name = create_modified_filename(file_name)
    write_file(new_file_name, 'im loving this module')
    
    new_content = read_file(new_file_name)
    print('Modified Content:', new_content)
    
except (FileNotFoundError, IOError) as e:
    print(f"Error: {e}")
    print(f"Please check '{file_name}' and try again.")
