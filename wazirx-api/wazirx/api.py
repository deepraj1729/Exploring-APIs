from wazirx.config import WazirxConfig
from wazirx.logger import Logger
import requests as req 
import json


class WazirxAPI:
    def __init__(self):
        self.all_cryptos = None
        self.GET()
    
    def GET(self):
        try:
            response = req.get(url=WazirxConfig.API.URL)
            self.all_cryptos = response.json()

            if str(response.status_code) == '404':
                Logger.error("Page not found! Error 404") 

        except Exception as e:
            Logger.error(e)


    def getAllCryptos(self):
        return self.retriveCryptoData("")

    def getINRCrypto(self):
        return self.retriveCryptoData("inr")

    def getUSDTCryptos(self):
        return self.retriveCryptoData("usdt")

    def getChange(self,last,open):
        change=0

        if open==0:
            change = "0"
            return change
        else:            
            change = ((last-open)/open)*100

        if change>=0:
            change = "+"+str(round(change,3))
        else:
            change = str(round(change,3))
        return change

    # Fomatted JSON output for a particular crypto
    def getCryptoInfo(self,crypto,id):
        crypto_data = self.all_cryptos[crypto]
        low=high=last=open=change=0
        crypto_dict = None
        low = float(crypto_data["low"])
        high = float(crypto_data["high"])
        last = float(crypto_data["last"])
        open = float(crypto_data["open"])
        change = self.getChange(last,open)

        if str(crypto)[-3:] == "inr":
            crypto_dict={
                    "id":id,
                    "name":crypto,
                    "exchange":"inr",
                    "low":low,
                    "high":high,
                    "last":last,
                    "open":open,
                    "change":change
                }

        elif str(crypto)[-4:] == "usdt":
            crypto_dict = {
                "id":id,
                "name":crypto,
                "exchange":"usdt",
                "low": low,
                "high":high,
                "last":last,
                "open":open,
                "change":change
            }
        return crypto_dict
    

    # Retrieve market data of a particular list of cryptos
    def retriveCryptoData(self,exchange=""):
        market=[]

        for id,crypto in enumerate(self.all_cryptos):
            data = self.getCryptoInfo(crypto,id)
            if data is None:
                continue

            if exchange == "" and data["last"]!=0:
                market.append(data)

            elif data["exchange"] == exchange and data["last"]!=0:
                market.append(data)
        return market


    # Save the api_data in a json file
    def saveJSON(self,data):
        filepath = WazirxConfig.IO.OUTPUT
        with open(filepath,"w") as f:
            json.dump(data,f,indent=6)
        f.close()
        Logger.success("Data retrieved saved to path: {}".format(filepath))