import os  # Import the os module for interacting with the file system
import shutil # Offers high-level operation on a file like a copy, create, remove, and remote operation on the file.

# Function to search for a file in the current directory and its subdirectories
def search(filename):
    for root, dirs, files in os.walk('.'):  # Walk through all directories and files starting from current directory
        if filename in files:  # If the target file is found
            path = os.path.join(root, filename)  # Create the full path to the file
            print(f"Found file at: {path}")  # Print the file's path
            with open(path, 'r') as file:  # Open the file in read mode
                print(file.read())  # Print the contents of the file
            return path  # Return the full path to the found file
    raise FileNotFoundError  # Raise error if file not found

# Function to handle the user's choice (modify, copy, delete)
def Next(choice, path):
    if choice.lower() == 'm':  # If choice is 'm' (modify)
        modify(path)  # Call modify function with the file path
    elif choice.lower() == 'c':  # If choice is 'c' (copy)
        copy(path)  # Call copy function with the file path
    elif choice.lower() == 'd':  # If choice is 'd' (delete)
        delete(path)  # Call delete function with the file path
    else:
        # Raise an error for any invalid choice
        raise AssertionError('Please make a choice that is available in this script! Don\'t forget to type the options in lowercase')

# Function to append user input to the end of the file without deleting anything
def modify(read):
    write = input('What would you like to write? ')  # Get user input to append to the file
    with open(read, 'r+') as write_file:  # Open file for reading and writing (must exist)
        write_file.seek(0, os.SEEK_END)  # Move the file pointer to the end of the file
        write_file.write(write + '\n')  # Write the input followed by a newline
        print('Content appended successfully.')  # Confirm to user
    return  # End the function

# Placeholder function for copying a file
def copy(cp):
    print(f"File to copy: {cp}")
    destination = input('Where would you like to put this copy? ')
    shutil.copy(cp, destination)
    print(f"Copied '{cp}' to '{destination}'.")

# Placeholder function for deleting a file
def delete(_del):
    print(f"File to delete: {_del}")
    final_choice = input('Are you sure you want to delete this file? (y/n) ')
    if final_choice.lower() == 'y':
         os.remove(_del)
         print(f"File '{_del}' deleted successfully.")
    elif final_choice.lower() == 'n':
        return
    else:
        raise AssertionError("Please type 'y' or 'n' in lowercase.")


# Main loop to interact with the user
try:
    while True:
        # Prompt the user for a file name
        searchfile = input("Enter the name of the file you want to display (or press Ctrl+C to exit): ")
        found_path = search(searchfile)  # Search for the file and get its path
        # Ask what to do with the file
        Next_Action = input('What would you like to do with {}? (m = modify, c = copy, d = delete) '.format(searchfile))
        Next(Next_Action, found_path)  # Call the action based on user input

# Handle keyboard interrupt (Ctrl+C)
except KeyboardInterrupt:
    print("\nExiting...")  # Exit message

# Handle if the file wasn't found
except FileNotFoundError as notfound_error:
    print('I apologize, but I am unable to locate the file.')
    raise notfound_error  # Re-raise the error to stop the program

# Handle general file-related errors
except OSError as os_error:
    print('Something went wrong, sorry.')
    raise os_error  # Re-raise the error

# Handle if the user enters an invalid option
except AssertionError as unclear_choice:
    print('Invalid choice.', unclear_choice)