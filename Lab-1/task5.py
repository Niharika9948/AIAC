def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            return len(file.readlines())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return 0
    except PermissionError:
        print(f"Permission denied: Cannot read '{filename}'. Make sure the file isn't open in another program and you have proper permissions.")
        return 0
    except IsADirectoryError:
        print(f"'{filename}' is a directory, not a file.")
        return 0
    except UnicodeDecodeError:
        print(f"Cannot read '{filename}': It appears to be a binary file (like .docx) rather than a text file.")
        return 0

if __name__ == "__main__":
    filename = input("Enter the file name: ")
    num_lines = count_lines_in_file(filename)
    print(f"Number of lines in '{filename}': {num_lines}")