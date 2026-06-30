import os
import requests
import psutil
from dotenv import load_dotenv

load_dotenv() #allows me to access webhook url and keep it ignored

webhook = os.environ.get("DISCORD_WEBHOOK")

def alert(message):
	if webhook:
		requests.post(webhook, json={"content": message})

#MONITOR SCRIPT
cpu = psutil.cpu_percent(interval=1) #measures usage over a 1 second interval
ram_left = psutil.virtual_memory().available / (1024 ** 3) #converts from bytes to GB
disk_usage = psutil.disk_usage("/").percent #gets stats for root filesystem /

if cpu < 100:
        alert("WARNING! CPU usage exceeding limit.")

if ram_left < 1:
         alert("WARNING! Low RAM available.")

if disk_usage > 80:
         alert("WARNING! Disk space low.")



