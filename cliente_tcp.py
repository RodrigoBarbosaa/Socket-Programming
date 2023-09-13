import socket
import time                                                

host = '127.0.0.1'
dns_port = 50003

# criando socket para conexão com dns
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servico_buscado = "calculadora_tcp"

udp_client_socket.sendto(servico_buscado.encode(), (host, dns_port))

data, addr = udp_client_socket.recvfrom(1024)
resposta = data.decode()

udp_client_socket.close()

#########################################################

lista_tempos_resposta = list()

if resposta == 'Not Found':
    print(f'Serviço de {servico_buscado} não encontrado')
    
else:
    print(f'Endereço do servidor {servico_buscado}: {resposta}')
    
    novo_host, nova_porta = resposta.split(':')
    novo_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print(f'Tentando conexão em {novo_host}: {nova_porta}')
    
    novo_socket.connect((novo_host, int(nova_porta)))
    
    pedidos = ['5 + 5', '10 * 3', '20 - 7', '40 / 5', '8 * 10'] # 5 solicitações
    
    
    for i in range(0, 5):
        
        print(f'Quanto é {pedidos[i]}?')
        
        inicio_contagem = time.perf_counter() # tempo
        
        novo_socket.send(pedidos[i].encode())
    
        resultado = novo_socket.recv(1024)
        
        fim_contagem = time.perf_counter() #tempo
        tempo_resposta = fim_contagem - inicio_contagem
        lista_tempos_resposta.append(tempo_resposta)

        print(f'{pedidos[i]} = {resultado.decode()}')
    
    novo_socket.close()
