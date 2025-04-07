from pathlib import Path  

def read_file(file_path):  
    try:  
        # Using a context manager to open a file  
        with open(file_path, 'r') as file:  
            content = file.read()  
            print("File content:\n", content)  
    except FileNotFoundError:  
        print(f"Error: The file {file_path} does not exist.")  
    except IOException as e:  
        print(f"An error occurred: {e}")  

def write_file(file_path, data):  
    try:  
        with open(file_path, 'w') as file:  
            file.write(data)  
            print(f"Data successfully written to {file_path}.")  
    except IOError as e:  
        print(f"An error occurred while writing to {file_path}: {e}")  

def main():  
    file_to_read = Path("example.txt")  
    data_to_write = "Hello, World!"  

    read_file(file_to_read)  
    write_file(file_to_read, data_to_write)  

if _name_ == "_main_":  
    main()git