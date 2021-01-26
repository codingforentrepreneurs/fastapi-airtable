from dotenv import load_dotenv
from functools import lru_cache
import os
import pathlib
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent # src

app = FastAPI()
templates = Jinja2Templates(directory = BASE_DIR / "templates" )

# http://localhost:3000/abc # route -> # path
# https://www.myawesomesite.com/abc

@lru_cache()
def cached_dotenv():
    load_dotenv()

cached_dotenv()


@app.get("/")
def home_view(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/")
def home_signup_view(request: Request, email:str = Form(...)):
    """
    TODO add CSRF for security
    """

    # to send email to airtable.
    
    return templates.TemplateResponse("home.html", {"request": request, "submitted_email": email})