from xml.etree.ElementInclude import include
import requests
import json
import os
from src.Logger import Logger
logger = Logger()
store_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'data', 'employers.json'))

def fetch_uhc_employers():
    logger.writeLogs("Job Started")
    url = "https://transparency-in-coverage.uhc.com/api/v1/uhc/blobs/"
    response = requests.get(url)
    data = []
    
    if response.status_code == 200:
        employers = json.loads(response.text)["blobs"]
        for index in range(len(employers)):
            if index == 100: break
            logger.writeLogs("Fetching Employer Index: {}".format(index))
            if "index" in employers[index]["name"]:
                response = requests.get(employers[index]["downloadUrl"])
                data.append(json.loads(response.text))

    with open(store_path, "w") as outfile:
        outfile.write(json.dumps(data))
    return []

def search_uhc_employers(type, search):
    f = open(store_path)
    employers = json.load(f)
    data = search_by_type(type, search, employers)
    return data

def search_by_type(type, text, employers):
    filtered = []
    valid = ['name', 'ein']
    if type not in valid: return filtered
    for index in range(len(employers)):
        employer = employers[index]
        property = employer["reporting_entity_name"] if type == 'name' else employer["reporting_structure"][0]["reporting_plans"][0]["plan_id"]
        if str(text).lower() in str(property).lower():
            filtered.append(employer)
    return filtered