
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def send_textMessage(driver, message):
    message_box_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
    message_box = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, message_box_path)))
    message_box.send_keys(message + Keys.ENTER)

def send_file(driver, audio_name):
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
        #time.sleep(1)
        send_btn.click()
    except NoSuchElementException:
        print('Error al enviar el audio')
        return False

    return True

# Export
def execute_action(driver, tipo_contenido, contenido):
    try:
        if tipo_contenido == 'textMessage':
            send_textMessage(driver, contenido)
        elif tipo_contenido == 'file':
            send_file(driver, contenido)
    except NoSuchElementException:
        print('Error al enviar la respuesta')
        return False
    time.sleep(1)
    return True