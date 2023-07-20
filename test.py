from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def iniciar_sesion():

    # Configura el controlador del navegador y abre WhatsApp Web
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get('https://web.whatsapp.com/')

    # Espera a que el usuario inicie sesión manualmente
    input('Inicia sesión en WhatsApp Web y presiona Enter para continuar...')
    return driver

def buscar_grupo(driver, nombre_grupo):
    # Espera a que se cargue la página de WhatsApp Web
    time.sleep(3)

    # Busca el grupo por su nombre y ábrelo
    search_box = driver.find_element("xpath", '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(nombre_grupo)
    search_box.send_keys(Keys.ENTER)

    # Espera a que se abra el grupo
    time.sleep(3)

    # Devuelve el objeto que representa la página del grupo
    return driver

def responder_comandos(driver):
    while True:
        # Espera para asegurarte de que se carguen los mensajes
        time.sleep(2)
        mensajes = driver.find_element("xpath", '//div[contains(@class,"copyable-text selectable-text")]')

        # Obtén el último mensaje
        ultimo_mensaje = mensajes[-1].text

        if ultimo_mensaje.startswith('*'):
            comando = ultimo_mensaje[1:]  # Elimina el prefijo "*"

            if comando == 'Horror':
                respuesta = 'BOOO'
            elif comando == 'Saludo':
                respuesta = 'Hola, ¿cómo están?'
            else:
                respuesta = 'Comando no reconocido.'

            # Envía la respuesta al grupo
            caja_de_texto = driver.find_element("xpath", '//div[@contenteditable="true"][@data-tab="6"]')
            caja_de_texto.send_keys(respuesta)
            caja_de_texto.send_keys(Keys.ENTER)

if __name__ == "__main__":
    grupo = "Lil s"  # Reemplaza con el nombre de tu grupo
    driver = iniciar_sesion()
    driver = buscar_grupo(driver, grupo)
    responder_comandos(driver)