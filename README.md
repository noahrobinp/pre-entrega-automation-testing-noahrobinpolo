Pre-Entrega – Automatización QA

Descripción del Proyecto
Este proyecto forma parte de la pre-entrega del curso de Automatización QA, abarcando los contenidos vistos hasta la Clase 8.
El objetivo principal es automatizar flujos básicos del sitio [https://www.saucedemo.com](https://www.saucedemo.com), aplicando buenas prácticas de testing automatizado con Python, Selenium WebDriver y Pytest.

Funcionalidades Automatizadas

* Inicio de sesión automático con credenciales válidas.
* Validación del acceso a la página de inventario.
* Verificación de productos visibles y del título de la página.
* Agregar un producto al carrito y validar el contador.
* Navegar al carrito y comprobar el producto agregado.

Tecnologías Utilizadas

* Python: lenguaje principal del proyecto.
* Selenium WebDriver: automatización del navegador.
* Pytest: framework para la ejecución de pruebas.
* WebDriver Manager: gestión automática del driver.
* Pytest-HTML: generación de reportes HTML.
* Git y GitHub: control de versiones y almacenamiento del repositorio.

Estructura del Proyecto
pre-entrega-automation-testing-noahrobinpolo/
│
├── tests/
│   ├── test_login.py          (pruebas de login)
│   └── test_inventory.py      (pruebas de inventario y carrito)
│
├── utils.py                   (funciones auxiliares y setup)
├── conftest.py                (configuración general de Pytest)
├── run_test.py                (script para ejecutar pruebas y generar reporte)
├── report.html            (reporte generado por Pytest)
|
│── assets/
│   └── style.css              (estilos para reportes o documentación)
|
|
└── README.md

Instalación de Dependencias
Ejecutar los siguientes comandos para instalar las librerías necesarias:
pip install selenium
pip install pytest
pip install webdriver-manager
pip install pytest-html

Ejecución de Pruebas
Para ejecutar todos los tests con reporte HTML:
pytest -v --html=reports/report.html --self-contained-html

Para ejecutar un test específico:
pytest tests/test_inventory.py -v

Reporte de Resultados
Al finalizar la ejecución se genera un reporte HTML que incluye:

* Casos ejecutados.
* Resultados (passed / failed).
* Tiempos de ejecución.
* Capturas de pantalla en caso de error (si aplica).

Objetivo del Proyecto
El propósito de esta automatización es:

* Aplicar buenas prácticas en el uso de Selenium WebDriver.
* Implementar una estructura modular utilizando Pytest.
* Validar el comportamiento del sitio web desde la perspectiva del usuario.
* Preparar el entorno para futuras automatizaciones más avanzadas.

Tester QA
Noah Robin Polo
Proyecto realizado para la materia Automatización QA 2025
