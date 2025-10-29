from selenium.webdriver.common.by import By
from selenium import webdriver


# Esta función prueba que el inventario (lista de productos) se muestre correctamente
def test_inventory(login_in_driver):  

    try:
        driver = login_in_driver

        # Verificamos que el título de la página sea el esperado tras el login
        assert driver.title == "Swag Labs"

        # Obtenemos todos los elementos con la clase 'inventory_item'
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        
        # Validamos que haya al menos un producto mostrado en el inventario
        assert len(products) > 0, "No hay productos visibles en la pagina"

        print("Hay productos visibles")

    except Exception as e:

        print(f"Error en test_inventory: {e}")
        raise

    finally:

        # Cerramos el navegador al finalizar la prueba (éxito o error)
        driver.quit()
        