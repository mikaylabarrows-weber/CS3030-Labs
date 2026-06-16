import subprocess
import re

result = subprocess.run(["w"], capture_output=True, text=True)
lines = result.stdout.splitlines()
users = []

for line in lines:

	if line.startswith("USER") or line.strip() == "":
		continue

	match = re.search(r"^(\w+)\s+(pts/\d+)", line)

	if match:
		username = match.group(1)
		terminal = match.group(2)

		users.append([username, terminal])

print("\nRecent Logins")
print("-" * 30)
print(f"{'USER':<15}{'TERMINAL':<15}")
print("-" * 30)

for user, terminal in users:
	print(f"{user:<15}{terminal:<15}")

# filtered out header lines so the regex only matches valid sessions (pts/X)
