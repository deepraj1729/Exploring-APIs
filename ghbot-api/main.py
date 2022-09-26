from github.bot import GhBot
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ContentBody(BaseModel):
    text: str

class ResponseBody(BaseModel):
    status: str
    message: str
    data: dict


@app.get("/api/v1/info")
def ghBot(username:str):
    try:
        bot = GhBot(username=username)
        data,status,msg = bot.getUserInfo()

        if status == "success":
            return ResponseBody(
                status = status,
                message = msg,
                data = data
            )
        else:
            return ResponseBody(
                status = "error",
                message = msg,
                data = data
            )

    except Exception as e:
        return ResponseBody(
            status = "failure",
            message = "error",
            data = {}
        )