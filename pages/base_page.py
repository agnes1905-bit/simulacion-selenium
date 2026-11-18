"""Clase base del patrón Page Object Model (POM)."""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def abrir(self, url):
        self.driver.get(url)

    def esperar_visible(self, localizador):
        return self.wait.until(EC.visibility_of_element_located(localizador))

    def esperar_clickeable(self, localizador):
        return self.wait.until(EC.element_to_be_clickable(localizador))

    def encontrar_todos(self, localizador):
        return self.driver.find_elements(*localizador)

    def titulo(self):
        return self.driver.title

    def url_actual(self):
        return self.driver.current_url
