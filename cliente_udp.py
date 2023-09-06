import socket
import time

udp_host = 'localhost'
udp_port = 50003

lista_tempos_resposta = list()

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

service_name = "calculadora_udp"

udp_client_socket.sendto(service_name.encode(), (udp_host, udp_port))

data, addr = udp_client_socket.recvfrom(1024)
response = data.decode()

udp_client_socket.close()

if response == "Not Found":
    print(f"Serviço '{service_name}' não encontrado.")
    
else:
    print(f"Endereço do servidor UDP para '{service_name}': {response}")

    # Cliente UDP para o servidor UDP obtido do servidor de nomes
    udp_host, udp_port = response.split(':')
    udp_client_socket.close()
     
    expression = ['5 + 5', '10 * 3', '20 - 7', '40 / 5', '8 * 10'] # 5 solicitações
    
    udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    
for i in range(0, 5):   
    
    print(f'Quanto é {expression[i]}?')
    
    inicio_contagem = time.perf_counter()
    
    udp_client_socket.sendto(expression[i].encode(), (udp_host, int(udp_port)))

    result = udp_client_socket.recvfrom(1024)
    
    fim_contagem = time.perf_counter()
    
    tempo_resposta = fim_contagem - inicio_contagem
    lista_tempos_resposta.append(tempo_resposta)
    
    print(f"{expression[i]} = {result[0].decode()}")

udp_client_socket.close()
