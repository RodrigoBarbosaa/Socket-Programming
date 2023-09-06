import socket

udp_host = 'localhost'
udp_port = 50005

socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_udp.bind((udp_host, udp_port))

print('Agurardando conexão de cliente')

try:
    for i in range(0, 5):
        data, address = socket_udp.recvfrom(1024)
        
        
        print(f'Conectado em: {address[1]}')
        
        pergunta = data.decode()
        
        if pergunta == '5 + 5':
            result = '10'
        elif pergunta == '10 * 3':
            result = '30'
        elif pergunta == '20 - 7':
            result = '13'
        elif pergunta == '40 / 5':
            result = '8'
        elif pergunta == '8 * 10':
            result = '80'
        else:
            result = 'not found'
            
        socket_udp.sendto(result.encode(), address)
   
except:
    socket_udp.close()
    
    
    