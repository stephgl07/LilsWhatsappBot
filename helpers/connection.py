from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def connect_to_existing_chrome(port):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", f"localhost:{port}")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def sign_in():
    # Conectarse a la instancia de Chrome ya abierta en el puerto 9222
    port = 9992
    driver = connect_to_existing_chrome(port)

    # Navega a WhatsApp Web
    # driver.get('https://web.whatsapp.com/')

    # Espera a que el usuario inicie sesión manualmente
    # input('Inicia sesión en WhatsApp Web y presiona Enter para continuar...')
    return driver

def search_groupchat(driver, chatName):
    # Busca el grupo por su nombre y ábrelo
    contact_path='//span[contains(@title,"'+ chatName +'")]'
    wait=WebDriverWait(driver,100)
    contact= wait.until(EC.presence_of_element_located((By.XPATH,contact_path)))
    contact.click()

    # Devuelve el objeto que representa la página del grupo
    return driver

# Export
def wsp_connect():
    chatName = "‼AVISOS‼"  # Reemplaza con el nombre de tu grupo
    driver = sign_in()
    driver = search_groupchat(driver, chatName)
    return driver