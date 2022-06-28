import requests as req

URL = "https://thecatapi.com/api/images/get?format=src&type=gif"

res = req.get(URL)

with open("cats/cat.gif", "wb") as f:
    print(res.headers)
    f.write(res.content)
f.close()
