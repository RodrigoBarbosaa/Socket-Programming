# Socket-Programming
Sockets programming using client-server architecture with TCP and UDP version

# Como executar o projeto? 

º Primeiro, deve-se abrir o servidor DNS ("dns.py") para começar a aceitar comunicação com os servidores UDP e TCP.

º Após isso, deve-se inicializar o servidor UDP ("servidor_udp.py") e servido TCP ("servidor_tcp.py") não necessariamente nessa ordem. 

º Dpois de abertos, irão se conectar automaticamente ao servidor dns, que armazenará seu serviço e a sua porta.

º Após o DNS salvar as informações dos servidores e os servidores tcp/udp estiverem aguardando conexões:
iniciar os clientes ("cliente_tcp.py") e ("cliente_udp.py"). Não necessariamente nessa ordem.

º Os clientes irão comunicar-se com o servidor DNS, que irá devolver a porta do servidor relativo ao serviço buscado. No caso do TCP: "calculadora_tcp" e do UDP: "calculadora_udp".

º Assim, os clientes entrarão em contato com o servidor respectivo fazendo 5 perguntas envolvendo soma, subtração, multiplicação e divisão. 

O servidor devolve a resposta para as 5 perguntas (feitas uma de cada vez) e o tempo é cronometrado para cada troca de mensagens.
Após concluída a comunicação, os serviços são encerrados e o DNS apaga os dados dos servidores de seu registro.

..
