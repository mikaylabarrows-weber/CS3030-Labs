def read_log(filename):
	with open(filename, "r") as file:
		for line in file:
			yield line

for line in read_log("large.log"):
	if "CRITICAL" in line:
		print(line.strip())

# Using yield allows Python to process one line at a time without absorbing too much memory!
# Using the .read() function can consume a lot of memory if used on a large file
