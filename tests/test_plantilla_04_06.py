"""Plantilla para los casos 04 a 06.
Reemplace el contenido según las funcionalidades reales del sitio
(login, búsqueda, formulario de contacto, etc.) y quite el decorador skip."""
import pytest
from pages.home_page import HomePage


@pytest.mark.skip(reason="Pendiente: completar con la funcionalidad real")
def test_04_funcionalidad_a(driver, url_base):
    """CP-04: <descripción>. Esperado: <resultado esperado>."""
    home = HomePage(driver, url_base)
    home.abrir_inicio()
    # 1) Realizar acciones mediante métodos del Page Object
    # 2) Obtener el resultado real
    # 3) assert resultado_obtenido == resultado_esperado


@pytest.mark.skip(reason="Pendiente: completar con la funcionalidad real")
def test_05_funcionalidad_b(driver, url_base):
    """CP-05: <descripción>. Esperado: <resultado esperado>."""


@pytest.mark.skip(reason="Pendiente: completar con la funcionalidad real")
def test_06_funcionalidad_c(driver, url_base):
    """CP-06: <descripción>. Esperado: <resultado esperado>."""
