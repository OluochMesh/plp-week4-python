file_name = input("Enter the file name/file path: ")
try:
    # Read the original file
    with open(file_name, 'r') as file:
        content = file.read()
        print("Original Content:", content)
    # Write modified content to a new file
    new_file_name = "modified_" + file_name
    with open(new_file_name, 'w') as new_file:
        new_file.write('im loving this module')
    # Read and print the modified file
    with open(new_file_name, 'r') as new_file:
        new_content = new_file.read()
        print('Modified Content:', new_content)
except (FileNotFoundError, IOError) as e:
    print(f"Error: {e}")
    print(f"Please check '{file_name}' and try again.")