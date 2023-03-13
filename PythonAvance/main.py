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
        "page": "Bienvenue sur DataMétéo"
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})

@app.get("/page/about", response_class=HTMLResponse)
async def page(request: Request):
    data = {
        "page": "About us",
        "soustitre": "Ynov informatique"
    }
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
        "page": "Analyse des données Météo France",
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


@app.get("/page/png/changement_temp", response_class=HTMLResponse)
async def page(request: Request):
    data = {
        "page": "Observe-t-on un un changement de températures dans le temps ?",
        "soustitre": "Explications :"
    }
    return templates.TemplateResponse("changement_temp.html", {"request": request, "data": data})


@app.get("/page/png/vents", response_class=HTMLResponse)
async def page(request: Request):
    data = {
        "page": "Il y a-t-il beaucoup de jours depuis 1996 où les éoliennes n'ont pas pu tourner ?",
        "soustitre": "Explications :"
    }
    return templates.TemplateResponse("vents.html", {"request": request, "data": data})

@app.get("/page/png/changement_semaine", response_class=HTMLResponse)
async def page(request: Request):
    data = {
        "page": "Observe-t-on des changements forts de températures au sein d'une semaine ?",
        "soustitre": "Explications :"
    }
    return templates.TemplateResponse("changement_semaine.html", {"request": request, "data": data})







