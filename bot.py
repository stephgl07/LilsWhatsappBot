from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from util.commands import COMANDOS_RESPUESTAS, RESPUESTA_POR_DEFECTO
import time
import os

def connect_to_existing_chrome(port):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", f"localhost:{port}")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def iniciar_sesion():
    # Conectarse a la instancia de Chrome ya abierta en el puerto 9222
    port = 9992
    driver = connect_to_existing_chrome(port)

    # Navega a WhatsApp Web
    # driver.get('https://web.whatsapp.com/')

    # Espera a que el usuario inicie sesión manualmente
    # input('Inicia sesión en WhatsApp Web y presiona Enter para continuar...')
    return driver

def buscar_grupo(driver, nombre_grupo):
    # Busca el grupo por su nombre y ábrelo
    contact_path='//span[contains(@title,"'+ nombre_grupo +'")]'
    wait=WebDriverWait(driver,100)
    contact= wait.until(EC.presence_of_element_located((By.XPATH,contact_path)))
    contact.click()

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

def send_audio(driver, audio_name):
    try:
        # Obtiene la ruta completa del archivo de audio dentro del proyecto
        audio_path = os.path.join(os.path.dirname(__file__), 'util', 'audio', audio_name)

        # Encuentra el campo de carga de archivos
        attachment_icon = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div')
        attachment_icon.click()

        # Espera a que aparezca la opción para enviar un audio
        imgsvids_input_path = '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'
        imgsvids_option = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, imgsvids_input_path)))
        imgsvids_option.send_keys(audio_path)

        # Envia el audio
        send_btn = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]')))
        send_btn.click()
    except NoSuchElementException:
        print('Error al enviar el audio')
        return False

    return True

def enviar_respuesta(driver, tipo_contenido, contenido):
    try:
        if tipo_contenido == 'textMessage':
            message_box_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
            message_box = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, message_box_path)))
            message_box.send_keys(contenido + Keys.ENTER)
        elif tipo_contenido == 'audio':
            # Envía el audio
            send_audio(driver, contenido)
    except NoSuchElementException:
        print('Error al enviar la respuesta')
        return False

    return True

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
                
                 # Busca el comando en el diccionario y obtiene su respuesta
                respuesta_info = COMANDOS_RESPUESTAS.get(comando, {'type': 'textMessage', 'content': RESPUESTA_POR_DEFECTO})
                tipo_contenido = respuesta_info['type']
                contenido = respuesta_info['content']

                # Envía la respuesta al grupo
                enviar_respuesta(driver, tipo_contenido, contenido)

        except Exception:
            # En caso de que no se encuentren elementos, se captura la excepción
            print("Ocurrio un error")
            continue

if __name__ == "__main__":
    grupo = "‼AVISOS‼"  # Reemplaza con el nombre de tu grupo
    driver = iniciar_sesion()
    driver = buscar_grupo(driver, grupo)
    responder_comandos(driver)