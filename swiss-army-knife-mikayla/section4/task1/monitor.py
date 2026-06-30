import psutil
import time #for the time loop for flashing

def warning(message):
	for _ in range(1):
		print(f"\033[5;91m{message}\033[0m")
		time.sleep(0.5)

cpu = psutil.cpu_percent(interval=1) #measures usage over a 1 second interval
ram_left = psutil.virtual_memory().available / (1024 ** 3) #converts from bytes to GB
disk_usage = psutil.disk_usage("/").percent #gets stats for root filesystem /

print(f"CPU Usage: {cpu:.1f}%") #formats the string to display the number to one decimal

if cpu > 80:
        warning("WARNING!")

print(f"RAM Available: {ram_left:.1f} GB")

if ram_left < 1:
	warning("WARNING!")

print(f"Disk Usage: {disk_usage:.1f}%")

if disk_usage > 80:
	warning("WARNING!")




