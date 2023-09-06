import socket
import threading

servico_oferecido = {
    "calculadora_tcp": ("localhost", 50000),
    "calculadora_udp": ("localhost", 50005)
}

host = 'localhost'
porta_tcp = 50002
porta_udp = 50003

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind((host, porta_tcp))
tcp_server_socket.listen()

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.bind((host, porta_udp))

print('DNS esperando por solicitações...')

def handle_udp_requests():   
    try:
        
        # Lida com solicitações UDP
        udp_request, udp_address = udp_server_socket.recvfrom(1024)
        udp_request = udp_request.decode()

        print(f'Solicitação UDP recebida de {udp_address}: {udp_request}')

        if udp_request in servico_oferecido:
            server_address = servico_oferecido[udp_request]
            print(f'Enviando endereço do servidor {udp_request}')
            response = f"{server_address[0]}:{server_address[1]}"
            udp_server_socket.sendto(response.encode(), udp_address)
            
        else:
            response = "Not Found"
            udp_server_socket.sendto(response.encode(), udp_address)
        
        udp_server_socket.close()
        
    except KeyboardInterrupt:
      pass
  
def handle_tcp_requests():
    try:  
        
        # Lida com solicitações TCP
        tcp_connection, tcp_address = tcp_server_socket.accept()
        print('Conexão TCP recebida de:', tcp_address)

        msg = 'Qual o serviço desejado?'
        tcp_connection.send(msg.encode())

        servico_buscado = tcp_connection.recv(1024).decode()
        print(f'Serviço buscado: {servico_buscado}')

        if servico_buscado in servico_oferecido:
            server_address = servico_oferecido[servico_buscado]
            print(f'Enviando endereço do servidor {servico_buscado}')
            response = f"{server_address[0]}:{server_address[1]}"
            tcp_connection.send(response.encode())
            
        else:
            response = "Not Found"
            tcp_connection.send(response.encode())

        tcp_connection.close()
        tcp_server_socket.close()
        
    except KeyboardInterrupt:
        pass
        

# Iniciar threads para lidar com solicitações UDP e TCP simultaneamente
udp_thread = threading.Thread(target=handle_udp_requests)
tcp_thread = threading.Thread(target=handle_tcp_requests)

udp_thread.start()
tcp_thread.start()

# Aguardar até que ambas as respostas sejam enviadas
udp_thread.join()
tcp_thread.join()