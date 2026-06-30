import requests

urls = ["https://google.com", "https://youtube.com", "http://thissiteisntreal123123.com"]

for url in urls:
	try:
		response = requests.get(url)

		if response.status_code == 200:
			print(url, " --> SITE UP")
		else:
			print(url, " --> SITE DOWN")

	except requests.exceptions.RequestException:
		print(url, " --> SITE DOWN")
