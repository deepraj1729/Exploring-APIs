class WazirxConfig:
    @staticmethod
    def buildURL(url, endpoint):
        return url+endpoint
    
    @staticmethod
    def buildPATH(path, filename):
        return path+filename

    class API:
        URL= "https://api.wazirx.com/api/v2/tickers"
        
    class IO:
        OUTPUT = "./output/"
        LOGS_PATH = "./logs/"