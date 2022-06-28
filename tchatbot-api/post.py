from chatBot.config import TChatBotConfig
from chatBot.logger import Logger
import requests as req
import argparse
import json

parser = argparse.ArgumentParser(description="POST request for GhBot")
version='1.0.0'

#Version
parser.add_argument('-v', action='version', version=version)
parser.add_argument('-u', type = str,help = "Your github username")

args = parser.parse_args()
username = args.u

#change .DEV_URL to PROD_URl for testing deployed production API
dev_url= TChatBotConfig.API.PROD_URL
endpoint = TChatBotConfig.API.ENDPOINT


url = TChatBotConfig.buildURL(dev_url,endpoint)

post_data = { "input":username }
headers = {'Content-type': 'application/json'}

res = req.post(url, data=json.dumps(post_data), headers=headers)
if res.status_code == 200:
    Logger.success("Request sent successfully")
    Logger.info(json.dumps(res.json(),indent=6))
else:
    Logger.error("Request failed with status code: {}".format(res.status_code))
    exit(1)