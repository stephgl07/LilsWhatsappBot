from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
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
    time.sleep(2)

    # Busca el grupo por su nombre y ábrelo
    contact_path='//span[contains(@title,"'+ nombre_grupo +'")]'
    wait=WebDriverWait(driver,100)
    contact= wait.until(EC.presence_of_element_located((By.XPATH,contact_path)))
    contact.click()

    # Espera a que se abra el grupo
    time.sleep(2)

    # Devuelve el objeto que representa la página del grupo
    return driver

def obtener_mensaje(chatContainer):
    try:
        # Encuentra todos los divs hijos de mensajes
        divs_hijos = chatContainer.find_elements(By.XPATH, 'div')

        # Obtén el último div de la lista
        ultimo_div = divs_hijos[-1]

        # Encuentra div 1ra Opcion
        try:
            div_contenedor_mensaje = ultimo_div.find_element(By.XPATH, './/div/div/div/div[2]/div[1]/div[2]/div/span[1]/span')
        except NoSuchElementException:
            div_contenedor_mensaje = ultimo_div.find_element(By.XPATH, './/div/div/div/div[1]/div[1]/div[1]/div/span[1]/span')

        # Encuentra el div que contiene el mensaje y obtén su texto
        ultimo_mensaje = div_contenedor_mensaje.text
        return ultimo_mensaje
    
    except Exception:
        # En caso de que no se encuentren elementos, se captura la excepción
        print('Error en obtencion de mensaje')

def responder_comandos(driver):
    # Espera para asegurarte de que se carguen los mensajes
    wait = WebDriverWait(driver, 100)
    time.sleep(1)
    while True:
        time.sleep(1)
        try:
            # Obtiene el div principal de los mensajes del chat
            chatContainer = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[3]')
            
            # Obtiene el ultimo mensaje del chat
            ultimo_mensaje = obtener_mensaje(chatContainer)

            # Valida si es o no un comando
            if ultimo_mensaje.startswith('*'):
                comando = ultimo_mensaje[1:]  # Elimina el prefijo "*"
                comando = comando.lower()
                if comando == 'sustito':
                    respuesta = 'BooOoOoO Ctm'
                elif comando == 'hola':
                    respuesta = 'Hola Bbcita'
                elif comando == 'holachupetin':
                    respuesta = 'Hola, gracias por contactarte conmigo, soy chupetin trujillo el mejor payasito del Perú. En estos momentos no puedo atenderte porque le estoy metiendo harta pinga a la zorra de tu madre dotero hediondo y la conchadetumadre'
                else:
                    respuesta = 'Comando no reconocido. Escribe bien mrd.'

                # Envía la respuesta al grupo
                try:
                    message_box_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
                    message_box = wait.until(EC.presence_of_element_located((By.XPATH, message_box_path)))
                    message_box.send_keys(respuesta + Keys.ENTER)
                except NoSuchElementException:
                    print('Error al obtener campo de texto')
                    continue

        except Exception:
            # En caso de que no se encuentren elementos, se captura la excepción
            print("Ocurrio un error")
            continue

if __name__ == "__main__":
    grupo = "Lil s"  # Reemplaza con el nombre de tu grupo
    driver = iniciar_sesion()
    driver = buscar_grupo(driver, grupo)
    responder_comandos(driver)