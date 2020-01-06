# Challenge-NW


Desafio ITOPS


Esse desafio tem como objetivo entender o seu conhecimento sobre o mundo de microserviços e containers.
Nós queremos construir uma API Hello World, efetuar o deploy em um container mínimo e expo-lo com um proxy reverso a frente (nginx) com suporte a TLS 1.2 utilizando certificado do letsencrypt.
São 4 desafios principais:

- Construir uma API extremamente basica retornando um Hello World em algum método HTTP (GET, POST, PUT...)
- Escrever um Dockerfile
- Automatizar o build do container
- Configurar TLS a frente do serviço

------------------------------------------------------------------------------

Realizei uma automação de todo processo, sendo adequado o desafio baseado em scripts e estudos na internet

Imagens do Docker

App | alpine-3.8
Nginx | latest

Requerimentos 

docker | docker-compose	| make

Definição dos detalhes do aplicativo

No ".env" é necessário inserir os detalhes do seu app.

# .env 
SSL_EMAIL=seuemail@example.com   # endereço de email do certificado 
Letsencrypt NGX_DOMAIN = myexample.com   # domínio da web para configuração do Nginx e Letsencrypt 
FLASK_ENV = development           # desenvolvimento / ambiente de produção do aplicativo python


SSL

Precisamos instalar o cliente Let's encrypt para obter os certificados SSL.

sudo make install-le-client

Ele instala o cliente Letsencrypt e obtém um certificado para o domínio da web especificado.

Nota: O certificado da Letsencrypt gratuito fica disponível apenas por 90 dias. Depois é necessário renovar

sudo make renew-le-cert

INICIAR

sudo make dc-start


Outros comandos

sudo make dc-reboot    # Reinicia o aplicativo. 
sudo make dc-stop      # Para o aplicativo. 
sudo make dc-cleanup   # Exclui e limpa as imagens do docker.
