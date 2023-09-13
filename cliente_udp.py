import socket
import time

# Conexão com o DNS
dns_host = 'localhost'
dns_port = 50003

lista_tempos_resposta = list()

udp_dns_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

service_name = "calculadora_udp"

udp_dns_socket.sendto(service_name.encode(), (dns_host, dns_port))

data, addr = udp_dns_socket.recvfrom(1024)
response = data.decode()

udp_dns_socket.close()

if response == "Not Found":
    print(f"Serviço '{service_name}' não encontrado.")
    
else:
    print(f"Endereço do servidor UDP para '{service_name}': {response}")

    # Cliente UDP para o servidor UDP obtido do servidor de nomes
    resposta_formatada = str(response)
    
    udp_host, udp_port = resposta_formatada.split(':')
     
    expression = ['5 + 5', '10 * 3', '20 - 7', '40 / 5', '8 * 10'] # 5 solicitações
    
    udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    
for i in range(0, 5):   
    inicio_contagem = time.perf_counter()
    
    udp_host = 'localhost'
    
    print(f'host: {udp_host} porta: {udp_port}')
    
    print(f'Quanto é {expression[i]}?')
    
    udp_client_socket.sendto(expression[i].encode(), (udp_host, int(udp_port)))

    result = udp_client_socket.recvfrom(1024)
    
    fim_contagem = time.perf_counter()
    
    tempo_resposta = fim_contagem - inicio_contagem
    lista_tempos_resposta.append(tempo_resposta)
    
    print(f"{expression[i]} = {result[0].decode()}")

udp_client_socket.close()
