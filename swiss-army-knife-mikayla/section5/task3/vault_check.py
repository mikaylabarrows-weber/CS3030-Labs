# Logic: Use python-dotenv to load the key. 
# The script should print: Accessing system with key: *******ABC. 
#     (Use string slicing or formatting to dynamically mask all but the last 3 characters of the key).

# The Audit: Run git status in your terminal. 
#     If your .env file shows up anywhere as an "untracked file" or a modified file, your audit fails! 
#     You must ensure .env is properly logged in your root .gitignore.

# Deliverable: A screenshot of your terminal running git status proving that .env is being actively ignored by your repository.

from dotenv import load_dotenv
import os
import subprocess

load_dotenv()

# Access and print key masked
api_key = os.getenv("SUPER_SECRET_KEY")

if api_key is None:
    print("ERROR: Key not found. Try again.")
else:
    masked_key = api_key[-3:].rjust(len(api_key), "*")
    print(f"Accessing system with key: {masked_key}")

# run git status in terminal
subprocess.run(["git", "status"])