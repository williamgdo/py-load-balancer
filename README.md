# py-load-balancer
A HTTP Load Balancer made in Python 

# Pré-requisitos

Python 3, Docker e Docker Compose instalados. 

Instalacao do docker

Primeiro esse link:
https://github.com/dcomp-leris/slice-enablers/tree/master/docker

Depois:
sudo apt -y install docker-compose docker-compose-plugin



# Instructions

Criar e selecionar um ambiente virtual para o load balancer

```bash
python3 -m venv env
source env/bin/activate
```

Instalar flask para fazer os servidores

```bash
pip install flask
```

Criar imagem e subir docker compose
```bash
sudo docker build -t server .
sudo docker-compose up -d
```

## Para cada processo

Atualmente, é necessário buildar localmente as duas imagens. Uma forma manual de fazer, é entrar em cada pasta (/load-balancer e /service) e usar o comando docker build. Exemplo:

```bash
# na pasta /load-balancer
sudo docker build -t load-balancer .
# na pasta service
sudo docker build -t power . 
```

Para executar as imagens é necessário que as duas estejam na mesma rede docker. Depois, é necessário redirecionar a porta padrão do container do load balancer. Por fim, é interessante dar um alias para os containers (parâmetro --name)
para que seja possível identificá-los sem ser por IP. Assim, um container com parametro "--name teste", pode ser chamado via `curl teste:5000`

```bash
sudo docker network create project
sudo docker run -p 7000:5000 --network projeto --name load-balancer load-balancer
sudo docker run --network projeto --name power1 power
curl localhost:7000
```

# Problemas

Depois de rodar `sudo docker run...` acabei encontrando um erro de que o container não desativava mesmo após encerrar com CTRL+C. É necessário excluir o container com comando `sudo docker rm <id-do-container>`. Mensagem de erro:

```
docker: Error response from daemon: Conflict. The container name "/power1" is already in use by container "8e785923686be79a2e0f3cc07928c865963d198fc9cd08d2964a611349fa3d35". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.
```
# Links interessantes

https://blog.devgenius.io/5-minutes-to-learn-python-and-create-your-own-load-balancer-step-by-step-tutorial-included-f3109b5f7961

https://testdriven.io/courses/http-load-balancer/routing/

https://dev.to/codemaker2015/build-and-deploy-flask-rest-api-on-docker-25mf

host-based vs path-based routing:
https://testdriven.io/courses/http-load-balancer/routing/