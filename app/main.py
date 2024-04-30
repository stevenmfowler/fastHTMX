from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

BASE_PATH = Path(__file__).resolve().parent
templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
def index(request:Request):
    context = {'request':request}
    return templates.TemplateResponse('pages/home.html',context)
