from NewsAPI.config import NewsConfig
from NewsAPI.logger import Logger
import requests as req
import json

API_KEY = NewsConfig.API.KEY

class NewsAPI:
    def __init__(self):
        pass

    def get_news(self,query, page_size):
        endpoint = f"?q={query}&pageSize={page_size}&apiKey={API_KEY}"
        url =NewsConfig.buildURL(url=NewsConfig.API.URL,endpoint=endpoint)
        res = req.get(url)
        if res.status_code == 200:
            self.data = res.json()
            Logger.success("Successfully fetched news")
            Logger.info(json.dumps(self.data,indent=6))
        else:
            Logger.error("Failed to fetch news")
            Logger.error(res.text)


    def saveJSON(self):
        path = NewsConfig.buildPATH(path=NewsConfig.IO.OUTPUT,filename="news.json")
        with open(path, "w") as f:
            json.dump(self.data, f, indent=6)
        Logger.success("Successfully saved data to file")
        Logger.info(f"File saved to {path}")