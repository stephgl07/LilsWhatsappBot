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