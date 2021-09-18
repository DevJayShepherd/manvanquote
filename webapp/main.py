from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from webapp.core.config import settings
from webapp.core.postcode_description import PostcodeBuilder
from webapp.core.postcodes import data

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
templates = Jinja2Templates(directory="webapp/templates")
app.mount("/webapp/static", StaticFiles(directory="webapp/static"), name="static")


@app.get("/")
def hello_api(request: Request):
    return templates.TemplateResponse(name="homepage.html", context={"request": request})


@app.get("/man-and-van/{location}")
def location_page(location: str, request: Request):
    postcode = location

    postcode_object = PostcodeBuilder()
    postcode_list = postcode_object.get_all_postcodes(postcode)

    item = location

    return templates.TemplateResponse(name="homepage.html", context={"request": request, "item": item, "postcode": postcode,
                                                                     "postcode_list": postcode_list})


@app.get("/sitemap")
def sitemap(request: Request):

    postcodes = data

    return templates.TemplateResponse(name="sitemap.html", context={"request": request, "postcodes": data})


@app.get("/sitemap-xml")
def sitemap(request: Request):
    return templates.TemplateResponse(name="sitemap.xml", context={"request": request})
