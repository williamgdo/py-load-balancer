# py-load-balancer

A HTTP Load Balancer made in Python
Made by:
William Giacometti
José Santana

# Dependências

Python 3, Docker e Docker Compose instalados.

Instalacao do docker

Primeiro esse link:
https://github.com/dcomp-leris/slice-enablers/tree/master/docker

Depois:
sudo apt -y install docker-compose-plugin

# Instruções

## Python

Para editar o serviço e o load balancer fora dos containers, é interessante usar um ambiente virtual para o python. Para criar e selecionar um ambiente virtual, use:

```bash
python3 -m venv env
source env/bin/activate
```

Instalar Flask para fazer os servidores e requests para fazer chamadas entre as APIs facilmente

```bash
pip install flask requests
```

## Docker

Comandos básicos:

- Para criar a imagem e subir os containers a primeira vez, use `sudo docker compose up -d`
- Para parar os containers, use `sudo docker compose stop`
- Para parar e removê-los, use `sudo docker compose down`

Caso deseje atualizar os apps após as imagens já tenham sido criadas, é necessessário buildar as imagens novamente e recriar os containers. Para isso, após as edições serem feitas, remova os containers e use o parâmetro --build no comando de `up` (para buildar a imagem e já subir) OU faça o build manualmente e depois suba os containers com as novas imagens.

Exemplo:

```bash
# após mudanças feitas em load-balancer.py ou service.py
sudo docker compose stop
sudo docker compose up --build -d
# OU
sudo docker compose stop
sudo docker compose build
sudo docker compose up -d
```

Para testar a aplicação, use algum programa para fazer requisições diretamente ao load balancer:

```bash
curl localhost:7000
curl -X POST -H "Content-Type: application/json" -d '{ "x":"2", "y":"4"}' http://localhost:7000/power
```

## MongoDB

A solução NoSQL escolhida foi MongoDB. Para criar uma imagem docker MongoDB, use:

```bash
# baixar imagem mongo:latest:
sudo docker pull mongo

# executar imagem em um container:
sudo docker run -d -p 27017:27017 --name mongo_example mongo

# entrar no container
sudo docker exec -it mongo_example bash
```
