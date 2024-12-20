#librerie per le impaginazioni
from tabulate import tabulate #libreria per la tabella
import os #libreria per pulire la console a inizio programma
os.system('clear') #pulizia console

import requests #libreria per le richieste HTML

url = "http://192.168.20.2/phpMyAdmin"

burp = {
    "http": "http://127.0.0.1:8080/",     #porta HTTP di ascolto su burp

}

#funzione richiesta GET
def getRequest(url):
    responseGET=requests.get(url, proxies=burp) #invio richiesta GET
    return responseGET

#Funzione richiseta POST
def postRequest(url):
    responsePOST=requests.post(url, proxies=burp)
    return responsePOST

#Funzione richiesta PUT
def putRequest(url):
    responsePUT=requests.put(url, proxies=burp)
    return responsePUT
#Funzione richiesta DELETE
def deleteRequest(url):
    responseDELETE=requests.delete(url, proxies=burp)
    return responseDELETE

#tabella che restituisce gli status codes
table=[
    ["GET request status code", getRequest(url).status_code], 
    ["POST request status code", postRequest(url).status_code],
    ["PUT request status code", putRequest(url).status_code],
    ["DELETE request status code", deleteRequest(url).status_code]
]
print(tabulate(table, tablefmt="grid"))