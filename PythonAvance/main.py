from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse, status_code=200)
async def home(request: Request):
    data = {
        "page": "Home page"
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})

@app.get("/page/about", response_class=HTMLResponse)
async def page(request: Request):
    data = {
        "page": "about",
        "soustitre": "aaaon est les meilleurs"
    }
    # return templates.TemplateResponse("base.html", {"request": request, "data": data})
    return templates.TemplateResponse("about.html", {"request": request, "data": data})

@app.get("/page/info", response_class=HTMLResponse)
async def page(request: Request):
    data = {
        "page": "info",
        "soustitre": "les infos"
    }
    return templates.TemplateResponse("info.html", {"request": request, "data": data})

@app.get("/page/png", response_class=HTMLResponse)
async def page(request: Request):
    data = {
        "page": "png",
        "soustitre": "les png"
    }
    return templates.TemplateResponse("png.html", {"request": request, "data": data})


@app.get("/page/png/annee_chaudes", response_class=HTMLResponse)
async def page(request: Request):
    data = {
        "page": "Quelles sont les 10 années les plus chaudes depuis 1996 ?",
        "soustitre": "Explications :"
    }
    return templates.TemplateResponse("annee_chaudes.html", {"request": request, "data": data})