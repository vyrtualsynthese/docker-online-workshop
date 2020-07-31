# Kata 1

## Installer docker

https://docs.docker.com/get-docker/

exemple pour Ubuntu:
```shell script
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io
```

Vérifier l'installation avec `docker --version`

Pouvoir utiliser Docker en non-root sous Linux: https://docs.docker.com/engine/install/linux-postinstall/
```
sudo groupadd docker # on ajoute le groupe docker si c'est pas déjà fait
sudo usermod -aG docker $USER # on s'ajoute dans le groupe docker
newgrp docker # active le groupe docker
```

## Mon premier container

`docker run -v $PWD/app.js:/app.js -p 3000:3000 node:alpine app.js`

Et rendez-vous sur http://127.0.0.1:3000, admirez ce joli Hello World avec Node dernière version.

Vous allez me dire: "pffeuh! jpeux faire pareil en plus simple avec `node app.js`."

Certes, mais est-ce que vous pouvez faire, dans un nouveau terminal, `docker run -v $PWD/app.js:/app.js -p 3001:3000 node:8-alpine app.js`? Ca vient de lancer le même serveur mais en Node versin 8!
C'est déjà plus compliqué de gérer plusieurs versions, n'est-ce pas ?

Allez, on lance un serveur web python: `docker run -it -v $PWD/app.py:/app.py -p 3002:3000 python:alpine python app.py`: http://127.0.0.1:3002 ?

Et un en PHP 7.2 `docker run -it -v $PWD/app.php:/var/www/html/index.php -p 3003:80 php:7.2-apache`: http://127.0.0.1:3003 ?

Vous venez de lancer 4 serveurs web en parallèle avec différents langages et versions sans rien d'autre que Docker!

Envie d'aller les voir? Suffit de lister les containers `docker ps`.



docker run : -v -p -w -u --rm -i -t --name 
docker ps
docker exec -it
docker inspect
docker rm
docker start
docker stop

docker images
docker rmi
docker build
docker tag

docker login
docker push
docker pull


* Dockerfile concepts: RUN FROM COPY ENTRYPOINT CMD WORKDIR ENV ARG
* docker-compose
* Multistage (buildkit)

