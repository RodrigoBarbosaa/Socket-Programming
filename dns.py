import socket

servico_oferecido = {}

udp_host = 'localhost'
porta_udp = 50003
conexoes_clientes = 0

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.bind((udp_host, porta_udp))

print('Servidor de Nomes esperando por solicitações de servidores...')

for c in range(2):
    data, addr = udp_server_socket.recvfrom(1024)
    dados = data.decode()
    servico, host, porta = dados.split(':')
    
    servico_oferecido[servico] = (host, porta) # nome do serviço e porta
    
    print(f'{data.decode()} adicionado ao DNS')

while True:
    data, addr = udp_server_socket.recvfrom(1024)
    service_name = data.decode()
    
    if service_name in servico_oferecido:
        
        
        server_address = servico_oferecido[service_name]
        response = f"{server_address[0]}:{server_address[1]}"
        
        print(f'Resposta enviada: {response}')
        
        udp_server_socket.sendto(response.encode(), addr)
        
        conexoes_clientes += 1
        
        if conexoes_clientes == 2:
            udp_server_socket.close()
            servico_oferecido.clear()
            break
    else:
        
        response = "Not Found"
        udp_server_socket.sendto(response.encode(), addr)
