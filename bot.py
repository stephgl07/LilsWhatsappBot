from helpers.connection import wsp_connect
from helpers.messageHandler import wsp_readmessages

if __name__ == "__main__":
    driver = wsp_connect()
    wsp_readmessages(driver)