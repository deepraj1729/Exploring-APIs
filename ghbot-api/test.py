import requests as req
from github.config import GhConfig
from github.loggers import Logger
import json

dev_url = GhConfig.API.DEV_URL
endpoint = GhConfig.API.ENDPOINT

url = GhConfig.buildURL(dev_url,endpoint)
username = "deepraj1729"

res = req.get(url+"?username="+username)
if res.status_code == 200:
    Logger.success("Request sent successfully")
    # Logger.info(json.dumps(res.json(),indent=6))


def getUnfollowers(user_data):
    followers = set(user_data["data"]["all_followers"])
    following = set(user_data["data"]["all_following"])
    notFollowingBack = list(following - followers)
    return notFollowingBack


print("Users not following back: ",getUnfollowers(res.json()))