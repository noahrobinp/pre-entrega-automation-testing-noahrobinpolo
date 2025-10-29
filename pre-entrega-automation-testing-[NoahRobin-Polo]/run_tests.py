import pytest

# Archivos de pruebas a ejecutar
test_files = [
"tests/test_login.py"
"tests/test_inventory.py"
]

# Argumentos para ejecutar pruebas: archivos y reporte html
pytest_args = test_files + ["--html=report.html","--self-contained-html","-v"]

pytest.main(pytest_args)