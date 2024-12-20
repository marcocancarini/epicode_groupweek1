import socket

SERVER_IP = "127.0.0.1" #Inserisci l'indirizzo IP del server
SERVER_PORT = 44444 #Inserisci il numero di porta

#Creo il mio socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Assegno al socket indirizzo e porta
mySocket.bind((SERVER_IP, SERVER_PORT))

#Ascolto le connessiomi in ingresso nel socket creato
mySocket.listen(1) #1 massimo numero di connessioni in coda

print("Server started, waiting for connections...")

#Accettiamo la connessione in ingresso verso il server
connection, address = mySocket.accept() #Address e' l'indirizzo IP del client in connessione

print("Client connected with address:", address)
print("Waiting for data...")

while 1:
    data = connection.recv(1024) #1024 grandezza del buffer da ricevere in byte
    if not data: break
    connection.sendall(b"-- Message received -- \n")
    #Stampo i dati decodificandoli in utf-8
    print(data.decode("utf-8"))
connection.close()