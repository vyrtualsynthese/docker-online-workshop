# Docker Online Workshop for NodeJS

##Step 0
When you run `docker --version` you will get something like: 

    Docker version 19.03.7, build 7141c199a2

Objective: You are able to install Docker  
Skills: Installing docker  
Useful links: https://docs.docker.com/get-docker/

##Step 1

Before playing with the provided small ExpressJS app, you will play with the Node REPL.

/!\ Remember to *NOT* use Node on your host but in Docker. 

When you *run* `os.hostname()` in the Node REPL you will get something like:

    'e9fb65b9d332'

Objective: You are able to run containers
Skills: Launch and run commands in containers.
Useful links: https://docs.docker.com/engine/reference/commandline/docker/


Solution: `docker run -it node node`


##Step 2

You have a small ExpressJS app (next to this file).

You have to install the dependencies of your app with `yarn install` to get it up in the next step.  
After, you should have a `node_modules` directory with `dotenv` and `express` inside.

Objective: You are able to bind volumes.
Skills: Bind volumes to mount host filesystem in a container.
Useful links: https://docs.docker.com/storage/volumes/


Solution: `docker run -v $(pwd):/app -w /app node yarn`


##Step 3

Expose Ports

This ExpressJS app reponds "Hello World" on each request.

When you execute `curl http://127.0.0.1:3000` on your host machine (or visit http://127.0.0.1:3000 in your browser), you should see:

    Hello World!


Skills: Dockerfile  
Useful Knowledge:

Solution: `docker run -v $(pwd):/app -w /app -p 3000:3000 node app.js`

##Step 4

Now you have a blocking process that run in a container.

Deletes the container.


Solution: `docker ps` `docker rm -f ...`

