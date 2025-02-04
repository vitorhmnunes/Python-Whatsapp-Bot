import requests 
from client import data_treatment as dt
import urllib
import time
import dotenv
import os


class ClientData():
    def __init__(self):
        self._client_data

    def getClient_data(self, row_index):
        self._client_data = dt.client_info(row_index)
        return self._client_data


class ClientName():
    def __init__(self):
        self._client_name
        self.data = ClientData()

    def getClient_name(self, row_index):
        data = self.data.getClient_data(row_index)
        self._client_name = data[0]
        return self._cliente_name


class ClientPhone():
    def __init__(self):
        self._client_phone
        self.data = ClientData()

    def getClient_phone(self, row_index):
        data = self.data.getClient_data(row_index)
        self._client_phone = data[1]
        return self._cliente_phone
    

class LoadDotEnv():
    def __init__(self):
        self._api_key
        self._bot_number

    def loadDotEnv(self):
        return dotenv.load_dotenv(dotenv.find_dotenv())

    def getApiKey(self):
        self.loadDotEnv()
        self._api_key = os.getenv('API_KEY')
        return self._api_key

    def getBotNumber(self):
        self.loadDotEnv()
        self._api_key = os.getenv('BOT_NUMBER')
        return self._api_key


class Messages():
    def __init__(self):
        self._client_name = ClientName()
        self._message_intro
        self._msg1 = "PRIMEIRA MENSAGEM"
        self._msg2 = "SEGUNDA MENSAGEM"
        self._msg3 = "TERCEIRA MENSAGEM"
        self._msg4 = "QUARTA MENSAGEM"
        self._msg5 = "QUINTA MENSAGEM"
        self._msgs_list = [self._msg1, self._msg2, self._msg3, self._msg4, self._msg5]
        self._product_message
        self._response_message
        
    def getProductMessage(self, row_index, index_message=1):
        self._message_intro = f"Olá, {self._client_name.getClient_name(row_index)}!!"
        self._product_message = self._message_intro + self._msgs_list[index_message]
        return self._product_message
        
    def getResponseAutoMessage(self):
        self._response_message = urllib.parse.quote(f"CLIENT RESPONSE AUTO MESSAGE")
        return self._response_message


class SendMessages():
    def __init__(self):
        self.env_dt = LoadDotEnv()
        self.message = Messages()
        self._client_phone = ClientPhone()
        self._url = f"https://gate.whapi.cloud/messages/interactive?{self.env_dt.getApiKey}"
        self.response
        self.payload
        self.headers

    def postMessage(self, msg_index, row_index):
        self.payload = {
                "typing_time": 4,
                "header": {"text": "TÍTULO DA MENSAGEM"},
                "body": {"text": self.message.getProductMessage(row_index, msg_index)},
                "action": {
                    "buttons": [
                        {"type": "url", "title": "TÍTULO DO BOTÃO", "id": "sim", "url": f"https://wa.me/{self.env_dt.getBotNumber()}/?text={self.message.getResponseAutoMessage()}"},
                        ]
                },
                "type": "button",
                "to": self._client_phone.getClient_phone(row_index) +"@s.whatsapp.net",
            }
        
        self.headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }
        
        self.response = requests.post(self._url, json=self.payload, headers=self.headers)
        

__name__ == "__main__"

send_message = SendMessages()

row_index = 0 #índice da linha inicial
x = 0
for i in dt.clientes4_df:

    send_message.postMessage(x, row_index)

    if x >= 4: #condicional para enviar todas as 5 mensagens pré-estabelecidas
        x = 0 
    else:
        x+=1

    time.sleep(10) #tempo de espera para o whatsapp não bloquear o bot

    print(row_index)
    print(send_message.response.text)
