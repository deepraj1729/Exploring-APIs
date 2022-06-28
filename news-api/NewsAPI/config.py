class NewsConfig:
    @staticmethod
    def buildURL(url, endpoint):
        return url+endpoint
    
    @staticmethod
    def buildPATH(path, filename):
        return path+filename

    class API:
        URL= f"https://newsapi.org/v2/everything"
        KEY = "b34d949713d74e749a3bf3de79d21781"

    class IO:
        OUTPUT = "./output/"
        LOGS_PATH = "./logs/"