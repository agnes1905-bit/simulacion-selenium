"""Casos de prueba automatizados CP-01 a CP-06 para GoodHomes (techmooncr.com/cityo).
Cada caso compara el resultado obtenido con el esperado mediante assert."""
from pages.home_page import HomePage, ELEMENTOS_MENU


def test_cp01_carga_pagina_principal(driver):
    """CP-01: La página principal carga. Esperado: la URL contiene techmooncr.com/cityo."""
    home = HomePage(driver)
    home.abrir_inicio()
    esperado = "techmooncr.com/cityo"
    obtenido = home.url_actual()
    assert esperado in obtenido, f"Esperado: contiene '{esperado}'. Obtenido: '{obtenido}'"


def test_cp02_titulo_de_la_pagina(driver):
    """CP-02: El título es el correcto."""
    home = HomePage(driver)
    home.abrir_inicio()
    esperado = "GoodHomes – A Contemporary Real Estate WordPress Theme"
    obtenido = home.titulo().strip()
    assert obtenido == esperado, f"Esperado: '{esperado}'. Obtenido: '{obtenido}'"


def test_cp03_menu_de_navegacion(driver):
    """CP-03: Aparecen los 6 elementos del menú."""
    home = HomePage(driver)
    home.abrir_inicio()
    esperado = ELEMENTOS_MENU
    obtenido = home.elementos_de_menu_presentes()
    assert obtenido == esperado, f"Esperado: {esperado}. Obtenido: {obtenido}"


def test_cp04_ir_a_about_us(driver):
    """CP-04: Al hacer clic en About Us, la URL contiene /about-us/."""
    home = HomePage(driver)
    home.abrir_inicio()
    home.ir_a_menu("About Us")
    esperado = "/about-us/"
    home.esperar_url_contiene(esperado)
    obtenido = home.url_actual()
    assert esperado in obtenido, f"Esperado: contiene '{esperado}'. Obtenido: '{obtenido}'"


def test_cp05_ir_a_contacts(driver):
    """CP-05: Al hacer clic en Contacts, la URL contiene /contacts/."""
    home = HomePage(driver)
    home.abrir_inicio()
    home.ir_a_menu("Contacts")
    esperado = "/contacts/"
    home.esperar_url_contiene(esperado)
    obtenido = home.url_actual()
    assert esperado in obtenido, f"Esperado: contiene '{esperado}'. Obtenido: '{obtenido}'"


def test_cp06_abrir_detalle_de_propiedad(driver):
    """CP-06: Al abrir la propiedad Multi Family House, la URL contiene su detalle."""
    home = HomePage(driver)
    home.abrir_inicio()
    home.abrir_primera_propiedad()
    esperado = "/properties/multi-family-house/"
    home.esperar_url_contiene(esperado)
    obtenido = home.url_actual()
    assert esperado in obtenido, f"Esperado: contiene '{esperado}'. Obtenido: '{obtenido}'"