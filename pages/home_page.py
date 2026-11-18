"""Page Object de la página principal de GoodHomes.
Los localizadores se concentran aquí: si el sitio cambia, solo se ajusta este archivo."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

URL_BASE = "https://techmooncr.com/cityo/"
ELEMENTOS_MENU = ["Home", "About Us", "Pricing", "Our Services", "FAQ", "Contacts"]


class HomePage(BasePage):
    CUERPO = (By.TAG_NAME, "body")
    ENLACES = (By.TAG_NAME, "a")
    PROPIEDAD = (By.CSS_SELECTOR, "a[href*='/cityo/properties/multi-family-house/']")

    def __init__(self, driver, url=URL_BASE):
        super().__init__(driver)
        self.url = url

    def abrir_inicio(self):
        self.abrir(self.url)
        self.esperar_visible(self.CUERPO)

    def textos_de_enlaces(self):
        """Lista con el texto de todos los enlaces de la página."""
        return [e.get_attribute("textContent").strip()
                for e in self.encontrar_todos(self.ENLACES)]

    def elementos_de_menu_presentes(self):
        """Devuelve cuáles de los 6 elementos esperados del menú existen."""
        textos = self.textos_de_enlaces()
        return [item for item in ELEMENTOS_MENU if item in textos]

    def ir_a_menu(self, texto):
        """Da clic en un elemento visible del menú por su texto."""
        localizador = (By.XPATH, f"//a[normalize-space()='{texto}']")
        elemento = self.primer_visible(localizador)
        assert elemento is not None, f"No se encontró el elemento de menú '{texto}'"
        self.clic(elemento)

    def abrir_primera_propiedad(self):
        """Abre el detalle de la propiedad 'Multi Family House' desde 'Newest Offers'."""
        elemento = self.primer_visible(self.PROPIEDAD)
        assert elemento is not None, "No se encontró la propiedad en la página"
        self.clic(elemento)