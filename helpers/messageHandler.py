import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from helpers.util.commands import COMANDOS_RESPUESTAS, RESPUESTA_POR_DEFECTO
from helpers.actionHandler import execute_action
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

def get_last_message(chatContainer):
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

# Export
def wsp_readmessages(driver):
    # Espera para asegurarte de que se carguen los mensajes
    wait = WebDriverWait(driver, 100)
    # Esperar hasta que el div principal de los mensajes del chat esté presente
    try:
        chatContainer = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[3]')))
    except NoSuchElementException:
        print('Error al obtener el contenedor del chat')

    while True:
        try:
            # Obtiene el ultimo mensaje del chat
            ultimo_mensaje = get_last_message(chatContainer)

            # Valida si es o no un comando
            if ultimo_mensaje.startswith('*'):
                comando = ultimo_mensaje[1:]  # Elimina el prefijo "*"
                comando = comando.lower()
                
                 # Busca el comando en el diccionario y obtiene su respuesta
                lst_actions = COMANDOS_RESPUESTAS.get(comando, RESPUESTA_POR_DEFECTO)
                for action in lst_actions:
                    tipo_contenido = action['type']
                    contenido = action['content']
                    # Envía la respuesta al grupo
                    execute_action(driver, tipo_contenido, contenido)


        except Exception:
            # En caso de que no se encuentren elementos, se captura la excepción
            print("Ocurrio un error al leer el contenedor del chat")
            continue