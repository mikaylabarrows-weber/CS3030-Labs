# In the real world, files get deleted, disks get full, and permissions change. Your script shouldn't just "crash"—
# it should fail gracefully and explain what happened.
# Code: Create robust_io.py in section5/task1/.

# Write a script that attempts to read a configuration file, modify a value, and write it back.
# The "Shield": Use a try...except...finally block. Crucial Rule: Order matters! You must catch specific errors first 
# and the general exception last:
    # FileNotFoundError (If the configuration file is missing).
    # PermissionError (If the current OS user doesn't have access).
    # Exception (The "catch-all" for any other unforeseen system errors).
# The "Finally": Use the finally block to print "Operation Attempted" regardless of success or failure.
# Deliverable: The script and a screenshot of the terminal showing your custom error message when you deliberately 
# try to read a non-existent file.

import configparser

config = configparser.ConfigParser()

try:
    # Reads the file!
    with open("fake.ini", "r") as file:
        config.read_file(file)

    # Changes a field in the file
    config["Settings"]["Username"] = "new_user"

    # Write the updated config back
    with open("fake.ini", "w") as file:
        config.write(file)

# Error Handling
except FileNotFoundError:
    print("ERROR: That file does not exist!")

except PermissionError:
    print("ERROR: You do not have permission to access this file!")

except Exception as e:
    print(f"ERROR: This function cannot be performed: {e}")

finally:
    print("Operation Attempted.")