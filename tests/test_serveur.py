import pytest
from PythonAvance.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    print(response.text[0])
    text_to_verify = '<h1>Welcome to FastAPI Starter.</h1>\nHome page'
    # assert response.text == text_to_verify #'{"page":"Home Page"}'
    assert text_to_verify in response.text
