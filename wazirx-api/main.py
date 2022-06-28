from wazirx.api import WazirxAPI
from wazirx.logger import Logger
import json

api = WazirxAPI()
data = api.getAllCryptos()
Logger.info(json.dumps(data,indent=6))
