import pytest
from PythonAvance.main import app
from fastapi.testclient import TestClient
import re
import os
from os import path

client = TestClient(app)


# def test_read_main():
#     response = client.get("/")
#     assert response.status_code == 200
#     print("print", response.text[:10])
#     text_to_verify = '<h1>Welcome to FastAPI Starter.</h1>\nHome page'
#     # assert response.text == text_to_verify #'{"page":"Home Page"}'
#     assert text_to_verify in response.text

# def test_png():
#     response = client.get("/page/png")
#     assert response.status_code == 200

#     pattern = '<h1 class="display-1">(.*?)<\/h1>'
#     result = re.search(pattern, response.text)

#     print("_______print_______")
#     print(result[1])
#     print("_______print_______")
#     title_to_try = "Analyse des données Météo France"
#     assert result[1] == title_to_try



def test_main_route():
    home = client.get("/")
    assert home.status_code == 200

    about = client.get("/page/about")
    assert about.status_code == 200

    png_card = client.get("/page/png")
    assert png_card.status_code == 200

    annee_chaudes = client.get("/page/png/annee_chaudes")
    assert annee_chaudes.status_code == 200

    changement_temp = client.get("/page/png/changement_temp")
    assert changement_temp.status_code == 200

    vents = client.get("/page/png/vents")
    assert vents.status_code == 200

    changement_semaine = client.get("/page/png/changement_semaine")
    assert changement_semaine.status_code == 200

def test_main_directory():
    # check if /static exist in current diretory 
    assert path.exists(os.path.join(os.path.abspath(os.getcwd()),"static"))

def test_png_title():
    response = client.get("/page/png")
    pattern = '<h1 class="display-1">(.*?)<\/h1>'
    result = re.search(pattern, response.text)
    title_to_try = "Analyse des données Météo France"
    assert result[1] == title_to_try

def test_home_title():
    response = client.get("/")
    pattern = '<h1 class="display-1">(.*?)<\/h1>'
    result = re.search(pattern, response.text)
    title_to_try = "Bienvenue sur DataMétéo"
    assert result[1] == title_to_try

