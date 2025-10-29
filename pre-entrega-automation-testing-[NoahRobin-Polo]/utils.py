from selenium.webdriver.common.by import By
import time

# Esta función realiza el proceso de login en la página de SauceDemo
def login(driver):

    # Abrimos la URL principal del sitio
    driver.get("https://www.saucedemo.com/")

    # Ingresamos el nombre de usuario en el campo correspondiente
    driver.find_element(By.ID,"user-name").send_keys("standard_user")

    # Ingresamos la contraseña en el campo correspondiente
    driver.find_element(By.ID,"password").send_keys("secret_sauce")

    # Hacemos clic en el botón de login
    driver.find_element(By.ID,"login-button").click()

    # Esperamos unos segundos para que se complete la carga de la página de inventario
    time.sleep(2)