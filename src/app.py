from fastapi import FastAPI

app = FastAPI()


# http://localhost:3000/abc # route -> # path
# https://www.myawesomesite.com/abc

@app.get("/")
def home_view():
    return {"hello": "world"}