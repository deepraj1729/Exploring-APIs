import requests as req
from github.bot import GhBot
from github.config import GhConfig
from github.loggers import Logger
import json
import time

OUTPUT_PATH = GhConfig.IO.OUTPUT+"following.json"
dev_url = GhConfig.API.DEV_URL
endpoint = GhConfig.API.ENDPOINT
url = GhConfig.buildURL(dev_url,endpoint)


def handleK(data):
    followers = data["followers"]
    following = data["following"]

    if "k" in data["followers"]:
        follower_arr = followers.split("k")
        data["followers"] = int(float(follower_arr[0])*1000)
    
    if "k" in data["following"]:
        following_arr = following.split("k")
        data["following"] = int(float(following_arr[0])*1000)
    
    else:
        data["followers"] = int(data["followers"])
        data["following"] = int(data["following"])
    
    return data



def saveFile(data):
    with open(OUTPUT_PATH,"w") as f:
        json.dump(data,f,indent=6)
    f.close()

def getUnfollowers(user_data):
    followers = set(user_data["data"]["all_followers"])
    following = set(user_data["data"]["all_following"])
    notFollowingBack = list(following - followers)
    return notFollowingBack

def sortByFollowing(data:list):
    newData = sorted(data, key=lambda d: int(d['following']),reverse=True)
    return newData

def scrapUserInfo(username):
    bot = GhBot(username=username)
    soup = bot.getSoup(f"https://github.com/{username}")
    user_data_list = soup.find_all("a",class_="Link--secondary no-underline no-wrap")
    follower_count = user_data_list[0].find_all("span",class_="text-bold color-fg-default")
    following_count = user_data_list[1].find_all("span",class_="text-bold color-fg-default")
    return follower_count[0].string,following_count[0].string


def getFollowingInfo(following_list):
    print("\n\n\n")
    following_data = {"info":[]}
    for idx,username in enumerate(following_list):
        follower_count,following_count = scrapUserInfo(username)
        modified_data = handleK({"username":username,"followers":follower_count,"following":following_count})
        following_data["info"].append(modified_data)
        print("[{}] user: {} followers: {} following: {}".format(idx+1,modified_data["username"],modified_data["followers"],modified_data["following"]))

    saveFile(following_data)
    return sortByFollowing(following_data["info"])


def printUsers(data:list):
    print("\n\n\n")
    for idx,user in enumerate(data):
        print("[{}] user: {} followers: {} following: {}".format(idx+1,user["username"],user["followers"],user["following"]))


if __name__ == "__main__":
    username = "deepraj1729"

    res = req.get(url+"?username="+username)
    if res.status_code == 200:
        Logger.success("Request sent successfully")

        user_data = res.json()
        following_list = user_data["data"]["all_following"]
        data = getFollowingInfo(following_list)
        printUsers(data)
