from dotenv import load_dotenv
from functools import lru_cache
import os
import pathlib
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from .airtable import Airtable
BASE_DIR = pathlib.Path(__file__).parent # src

app = FastAPI()
templates = Jinja2Templates(directory = BASE_DIR / "templates" )

# http://localhost:3000/abc # route -> # path
# https://www.myawesomesite.com/abc

@lru_cache()
def cached_dotenv():
    load_dotenv()

cached_dotenv()

AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_TABLE_NAME = os.environ.get("AIRTABLE_TABLE_NAME")



@app.get("/")
def home_view(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/")
def home_signup_view(request: Request, email:str = Form(...)):
    """
    TODO add CSRF for security
    """

    # to send email to airtable.
    airtable_client =  Airtable(
        base_id=AIRTABLE_BASE_ID,
        api_key=AIRTABLE_API_KEY,
        table_name=AIRTABLE_TABLE_NAME,
    )
   
    did_send = airtable_client.create_records({"email": email})
    return templates.TemplateResponse("home.html", {"request": request, "submitted_email": email, "did_send": did_send})