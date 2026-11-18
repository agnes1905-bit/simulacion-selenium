"""Casos de prueba 01 a 03 (genéricos; funcionan como base y se deben ajustar al sitio)."""
from pages.home_page import HomePage


def test_01_carga_pagina_principal(driver, url_base):
    """CP-01: La página principal carga correctamente.
    Esperado: la URL contiene 'techmooncr.com'."""
    home = HomePage(driver, url_base)
    home.abrir_inicio()
    assert "techmooncr.com" in home.url_actual()


def test_02_titulo_no_vacio(driver, url_base):
    """CP-02: La página tiene un título.
    Esperado: el título no está vacío."""
    home = HomePage(driver, url_base)
    home.abrir_inicio()
    assert home.titulo().strip() != ""


def test_03_existen_enlaces_de_navegacion(driver, url_base):
    """CP-03: La página muestra enlaces de navegación.
    Esperado: al menos 1 enlace."""
    home = HomePage(driver, url_base)
    home.abrir_inicio()
    assert home.cantidad_enlaces() >= 1
