import re

with open("sample.log", "r") as file:
	log_data = file.read()

ip_pattern = r"\d+\.\d+\.\d+\.\d+"
timestamp_pattern = r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}\]"

ipresults = re.findall(ip_pattern, log_data)
timeresults = re.findall(timestamp_pattern, log_data)

print ("IP Addresses in File: ")
for ip in ipresults:
	print(ip)

print ("\nTimestamps in File: ")
for timestamp in timeresults:
	print(timestamp)

