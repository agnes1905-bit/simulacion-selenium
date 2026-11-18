# Simulación: Mi primera ejecución de pruebas

Automatización de pruebas con Selenium WebDriver (Python + pytest) usando el patrón Page Object Model.

## Instalación
```
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
pip install -r requirements.txt
```

## Ejecución
```
pytest
```
El reporte HTML queda en `reports/reporte.html`.

## Estructura
- `pages/`: Page Objects (BasePage, HomePage)
- `tests/`: casos de prueba
- `conftest.py`: configuración del navegador
