import re
import csv

rows = []
pattern = r"\[(.*?)\]\s+(ERROR)\s+(.*)"

with open("sample.log", "r") as file:
	for line in file:
		if "ERROR" in line:
			match = re.search(pattern, line)
			if match:
				date = match.group(1)
				error_type = match.group(2)
				message = match.group(3)

				rows.append([date, error_type, message])

with open("error_report.csv", "w", newline="") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["Date", "Error Type", "Message"])
	writer.writerows(rows)

print("Error report generated: error_report.csv")

