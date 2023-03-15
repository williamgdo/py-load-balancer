# py-load-balancer
A HTTP Load Balancer made in Python 

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

* Para criar a imagem e subir os containers a primeira vez, use `sudo docker compose up -d`
* Para parar os containers, use `sudo docker compose stop`
* Para parar e removê-los, use `sudo docker compose down`


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
```
# Links interessantes

https://blog.devgenius.io/5-minutes-to-learn-python-and-create-your-own-load-balancer-step-by-step-tutorial-included-f3109b5f7961

https://testdriven.io/courses/http-load-balancer/routing/

https://dev.to/codemaker2015/build-and-deploy-flask-rest-api-on-docker-25mf

host-based vs path-based routing:
https://testdriven.io/courses/http-load-balancer/routing/

docker compose cheatsheet https://github.com/tldr-pages/tldr/blob/master/pages/common/docker-compose.md

https://www.youtube.com/watch?v=CSb-sHNM2NY


