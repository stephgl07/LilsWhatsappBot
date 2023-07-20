# WhatsApp Bot con Selenium

Este proyecto es un script de Python que utiliza la biblioteca Selenium para crear un bot automatizado para WhatsApp Web. El bot puede iniciar sesión en WhatsApp Web, abrir un grupo específico y responder a comandos predefinidos dentro del grupo.

## Instrucciones de Uso

### Instalación

- Asegúrate de tener instalado Python en tu sistema. Puedes descargarlo desde el sitio web oficial de Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)

- Instala la biblioteca Selenium. Puedes hacerlo ejecutando el siguiente comando en tu terminal o símbolo del sistema:

    ```cmd
    pip install selenium
    ```

- Descarga el controlador del navegador Chrome adecuado para tu sistema operativo desde el sitio web oficial de ChromeDriver: [https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)

- Descomprime el archivo descargado y coloca el archivo ejecutable `chromedriver` en una ubicación accesible en tu sistema. Asegúrate de que la versión de ChromeDriver coincida con la versión de Google Chrome que tienes instalada.
    - El archivo ejecutable del driver puede ser ingresado en la ruta `C:\WebDriver` y luego agregado en el parametro PATH de las variables de entorno del sistema. 
    - Para verificar que este haya sido agregado exitosamente, puedes ejecutar el siguiente comando en tu terminal o símbolo del sistema:
        ```cmd
        chromedriver.exe --version
        ```
        Si fue agregado exitosamente, se podrá visualizar la versión del driver.
- Actualmente, este proyecto ha sido probado usando las siguientes versiones:
    - Google Chrome: 110.0.5481.78
    - ChromeDriver: 110.0.5481.77

    Ambos instaladores pueden ser encontrados en el siguiente enlace:
    https://drive.google.com/drive/folders/1HGAuuhUsIt9x4OH6E8ncTda6-YZ-nYuA?usp=sharing

### Configuración

- Abre el archivo `commands.py` y define los comandos y sus respuestas según tus necesidades. Por ejemplo:

```python 
# commands.py

COMANDOS_RESPUESTAS = {
    'sustito': 'BooOoOoO Ctm',
    'hola': 'Hola Bbcita',
    'holachupetin': 'Hola, gracias por contactarte conmigo, soy chupetin trujillo el mejor payasito del Perú...',
    # Agrega aquí más comandos y respuestas si deseas
}
```

En el archivo principal bot.py, asegúrate de que la variable grupo esté configurada con el nombre del grupo al que deseas que el bot responda. Por ejemplo:

```python 
# bot.py

grupo = "Nombre del Grupo"  # Reemplaza con el nombre de tu grupo
```

### Ejecución

Abre una terminal o símbolo del sistema en la ubicación del proyecto donde se encuentran los archivos bot.py y commands.py.

Ejecuta el script bot.py usando el comando:

```python 
bot.py
```

Aparecerá una ventana del navegador Chrome que abrirá WhatsApp Web. Se te pedirá que inicies sesión manualmente en WhatsApp Web.

Una vez que hayas iniciado sesión, el bot buscará el grupo configurado y estará listo para responder a los comandos en el chat del grupo.

### Funcionamiento

Cuando envíes un mensaje en el grupo que comience con un asterisco ("*"), el bot interpretará ese mensaje como un comando y responderá automáticamente con la respuesta predefinida correspondiente. Si el comando no es reconocido, el bot enviará un mensaje indicando que el comando no es válido.

Puedes modificar los comandos y sus respuestas en el archivo commands.py sin necesidad de modificar el archivo principal bot.py. Esto facilita la personalización del bot según tus preferencias.

### Advertencia

Ten en cuenta que el uso de bots para enviar mensajes automatizados en WhatsApp puede violar los términos de servicio de WhatsApp. Utiliza este bot con responsabilidad y asegúrate de cumplir con las políticas y condiciones de uso de WhatsApp.

WhatsApp Web puede cambiar su estructura o políticas en cualquier momento, lo que podría afectar el funcionamiento del bot. Mantente actualizado y revisa si hay cambios necesarios para adaptar el código si surge algún problema.

¡Listo! Ahora tienes un bot automatizado de WhatsApp que puede responder a comandos específicos en un grupo. Disfruta y experimenta con él, y siéntete libre de agregar más comandos y funcionalidades según tus necesidades.