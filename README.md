# CHALLENGE-NW :trophy:


## Desafio ITOPS :arrows_clockwise:


Esse desafio tem como objetivo entender o seu conhecimento sobre o mundo de microserviços e containers. Nós queremos construir uma API Hello World, efetuar o deploy em um container mínimo e expo-lo com um proxy reverso a frente (nginx) com suporte a TLS 1.2 utilizando certificado do letsencrypt. São 4 desafios principais:

- Construir uma API extremamente basica retornando um Hello World em algum método HTTP (GET, POST, PUT...)
- Escrever um Dockerfile
- Configurar TLS a frente do serviço
- Automatizar o build do container

------------------------------------------------------------------------------
### Descrição

Fala Time, irei descrever aqui as etapas deste **desafio**, ***MUITO*** desafiador (kkk)

Segui a ordem que esta descrita acima na introdução sendo que a ultima parte não consegui infelizmente não consegui realizar =/

Todo projeto foi baseado em estudo e pesquisa na internet, junto do meu conhecimento.

#### Desenvolvimento da API (Python) :snake:

A API desenvolvida mostra uma pagina HTML com um texto e uma imagem .gif, sendo que se acessar qualquer outro subdominio no site é mostrado uma pagina de erro e um indicativo para voltar a home, também foi criar um script do Gunicorn para realizar o balanceamento de carga.

#### Criação do Dockerfile  :memo:

Os Dockerfile's foram criados contendo apenas o conteudo essencial para funcionamento da API e sua segurança tendo abaixo sua especificações

|   Serviço| Imagem   | Versão   |
| ------------ | ------------ | ------------ |
| Flask e Gunicorn  | alpine  |  3.7 |
|  Nginx  |  nginx | mais recente |

#### Configuração do TLS

Confesso essa foi a parte mais complexa para mim, por mais que existam diversos tutoriais na internet, realizar a integração dentro do Docker me custou muito para compreender, até que consegui um script que automatiza :fa-heart: todo o processo, fiz um code review validando toda a estrutura e ficou uma belezinha. =P

####  Como usar 


#### - Definição dos detalhes da aplicação

O `.env` precisa ser editado para inserir as informações do certificado
```sh
# .env
SSL_EMAIL=meuemail@example.com  # email para o certificado Letsencrypt 
NGX_DOMAIN=meusite.com  # Endereço para o Nginx setar junto com o Letsencrypt
FLASK_ENV=development          # Setar qual ambiente será usado produção ou dev
```

#### - SSL
Comandos para realizar a validação do Letsencrypt client gerando o certificado SSL
```sh
sudo make install-le-client
```
Instala o cliente Letsencrypt e obtém um certificado para o domínio da web especificado.

_Obs: O Letsencrypt é validado apenas por 90 dias, sendo necessário renovar com o comando abaixo:_   
```sh
sudo make renew-le-cert
```

## :fast_forward:  Tudo Okay, Let's Go

**Iniciar aplicação**
```sh
sudo make dc-start
```
A ultima etapa de automatizar (Ansible + Github Webhooks) não consegui realizar. :persevere::disappointed:
