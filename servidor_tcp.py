import socket 
import time 

host = 'localhost'
port = 50000

# criando socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# definido valores e colocando no modo de escuta
s.bind((host, port))
s.listen()
print('Agurardando conexão de cliente')

# aceitando a conexão
connection, address = s.accept()
print(f'Conectado em: {address}')

# trocando mensagens
while True:
    
    data = connection.recv(1024)
    
    if not data:
        print('Fechando a conexão')
        connection.close()
        break
    
    expressao = data.decode()
    
    if expressao == '5 + 5':
        result = '10'
    elif expressao == '10 * 3':
        result = '30'
    elif expressao == '20 - 7':
        result = '13'
    elif expressao == '40 / 5':
        result = '8'
    elif expressao == '8 * 10':
        result = '80'
    else:
        result = 'not found'
    
    connection.send(result.encode())
    

