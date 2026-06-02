import subprocess

def unsafe_run(user_input):
	subprocess.run(f"echo{user_input}", shell=True)
def safe_run(user_input):
	subprocess.run(["echo", user_input]}

unsafe_run("Test Test")
safe_run("Test Test")
# Using shell=True could mean the user can insert special characters that may be interpreted as additional commands.
# Input validation is critical to avoiding exploitation. This can convert user input to being
# interpreted as data rather than commands
