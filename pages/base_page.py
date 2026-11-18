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

    def esperar_url_contiene(self, fragmento):
        """Espera hasta que la URL contenga el fragmento. Devuelve True/False."""
        try:
            return self.wait.until(EC.url_contains(fragmento))
        except Exception:
            return False

    def encontrar_todos(self, localizador):
        return self.driver.find_elements(*localizador)

    def primer_visible(self, localizador):
        """Devuelve el primer elemento visible que coincida con el localizador."""
        for elemento in self.encontrar_todos(localizador):
            if elemento.is_displayed():
                return elemento
        return None

    def clic(self, elemento):
        """Hace scroll hasta el elemento y da clic (con JavaScript como respaldo)."""
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", elemento)
        try:
            elemento.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", elemento)

    def titulo(self):
        return self.driver.title

    def url_actual(self):
        return self.driver.current_url