from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from core.config import settings
from core.postcodes import data

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
templates = Jinja2Templates(directory="templates")
app.mount("/webapp/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def hello_api(request: Request):
    return templates.TemplateResponse(name="homepage.html", context={"request": request})


@app.get("/man-and-van/{location}")
def location_page(location: str, request: Request):

    item = location

    return templates.TemplateResponse(name="homepage.html", context={"request": request, "item": item})


@app.get("/sitemap")
def sitemap(request: Request):

    postcodes = data

    return templates.TemplateResponse(name="sitemap.html", context={"request": request, "postcodes": data})
