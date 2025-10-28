# Importamos las librerías necesarias de Selenium y la librería time para manejar pausas
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Definimos una función de prueba para verificar el login en el sitio SauceDemo
def test_login():  

    # Inicializamos el navegador (en este caso, Google Chrome)
    driver = webdriver.Chrome()
    
    try:

        # Abrimos la página principal de SauceDemo
        driver.get("https://www.saucedemo.com/")

        # Esperamos un momento para que cargue la página
        time.sleep(1)

        # Localizamos los campos de usuario y contraseña y enviamos las credenciales correctas
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.ID,"password").send_keys("secret_sauce")

        # Localizamos y hacemos clic en el botón de login
        driver.find_element(By.ID,"login-button").click()

        # Esperamos a que se complete la redirección
        time.sleep(2)

         # Verificamos que la URL actual contenga "/inventory.html" (indicando un login exitoso)
        assert "/inventory.html" in driver.current_url, "No se redirigio correctamente al inventario"

        # Si todo salió bien, mostramos un mensaje de éxito
        print("Login exitoso y validado correctamente")

    except Exception as e:

         # Si ocurre algún error, lo mostramos por consola
        print(f"Error en test_login: {e}")
        
        raise