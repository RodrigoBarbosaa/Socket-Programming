import socket
import time                                                

host = '127.0.0.1'
port = 50002

lista_tempos_resposta = list()

# criando socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servico_buscado = 'calculadora_tcp'

# solicitando conexão com o servidor
s.connect((host, port))

pergunta_dns = s.recv(1024).decode()
print(f'{pergunta_dns}')

print('calculadora_tcp')

# enviando busca por serviço
s.sendall(servico_buscado.encode())

# recebendo resposta do servidor dns
resposta = s.recv(1024).decode()

s.close()


if resposta == 'Not Found':
    print(f'Serviço de {servico_buscado} não encontrado')
    
else:
    print(f'Endereço do servidor {servico_buscado}: {resposta}')
    
    novo_host, nova_porta = resposta.split(':')
    novo_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    novo_socket.connect((novo_host, int(nova_porta)))
    
    pedidos = ['5 + 5', '10 * 3', '20 - 7', '40 / 5', '8 * 10'] # 5 solicitações
    
    
    for i in range(0, 5):
        
        print(f'Quanto é {pedidos[i]}?')
        
        inicio_contagem = time.perf_counter()
        
        novo_socket.sendall(pedidos[i].encode())
    
        resultado = novo_socket.recv(1024)
        
        fim_contagem = time.perf_counter()
        tempo_resposta = fim_contagem - inicio_contagem
        lista_tempos_resposta.append(tempo_resposta)

        print(f'{pedidos[i]} = {resultado.decode()}')
    
    novo_socket.close()
