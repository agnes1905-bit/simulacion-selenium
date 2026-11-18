"""Page Object de la página principal.
Ajuste los localizadores según el HTML real del sitio (clic derecho > Inspeccionar)."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    CUERPO = (By.TAG_NAME, "body")
    ENLACES = (By.TAG_NAME, "a")
    IMAGENES = (By.TAG_NAME, "img")
    # TODO: agregar localizadores propios del sitio (menú, buscador, formulario, etc.)

    def __init__(self, driver, url):
        super().__init__(driver)
        self.url = url

    def abrir_inicio(self):
        self.abrir(self.url)
        self.esperar_visible(self.CUERPO)

    def cantidad_enlaces(self):
        return len(self.encontrar_todos(self.ENLACES))

    def cantidad_imagenes(self):
        return len(self.encontrar_todos(self.IMAGENES))
