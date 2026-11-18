"""Configuración compartida: crea y cierra el navegador para cada prueba."""
import pytest
from selenium import webdriver

URL_BASE = "https://techmooncr.com/cityo"  # Cambiar si usa otro sitio


@pytest.fixture
def driver():
    opciones = webdriver.ChromeOptions()
    opciones.add_argument("--start-maximized")
    # opciones.add_argument("--headless=new")  # Descomentar para correr sin ventana
    navegador = webdriver.Chrome(options=opciones)
    navegador.implicitly_wait(5)
    yield navegador
    navegador.quit()


@pytest.fixture
def url_base():
    return URL_BASE
