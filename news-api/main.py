from NewsAPI.api import NewsAPI

api = NewsAPI()
api.get_news("bitcoin", 10)
api.saveJSON()