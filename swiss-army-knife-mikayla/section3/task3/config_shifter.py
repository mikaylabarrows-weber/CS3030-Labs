import json
import yaml

config = {
	"server": "prod",
	"port": 80,
	"status": "active"
}

with open("config.json", "w") as json_file:
	json.dump(config, json_file, indent=4)

with open("config.json", "r") as json_file:
	config_data = json.load(json_file)

config_data["status"] = "maintenance"

with open("config.yaml", "w") as yaml_file:
	yaml.dump(config_data, yaml_file)

print("config.json created")
print("config.yaml created")
