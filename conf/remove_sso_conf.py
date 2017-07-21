import json

with open("/etc/ssowat/conf.json.persistent", "r") as jsonFile:
    data = json.load(jsonFile)
    data["skipped_urls"].remove("/_matrix")

with open("/etc/ssowat/conf.json.persistent", "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent=4, sort_keys=True))