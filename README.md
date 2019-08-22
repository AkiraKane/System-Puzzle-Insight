# System-Puzzle-Insight
Thought process and debugging system puzzle for Insight DevOps program


## 1. Understanding the Compments of the Architecture

In this project, the developer is using Postgres for the backend database, the Python Flask framework as an application server, and Nginx as a web server. The general Architecture diagram looks like the following:

<p align="center"><img src="images/logo.png" style="height: 100%; width: 100%; max-width: 200px" /></p>

Nignx is a web server that handles HTTP requests that come from the clients. Based on how you configure Nginx, it can directly provide the static connect back to the clients. Additionally, it can reverse proxy the requests to the WSGI (Gunicorn, Apache, etc) server to generate the dynamic content in the Flask web application to be delivered back to the user.

Briefly underderstanding the usage of each components, next step is to run the containers and debug the errors.

## 2.Degbuggig the whole Architecture

Docker Compose is a tool for defining and running multi-container Docker applications. In our `docker-compose.yml` file, we have about 4 main services:

 * db: our Postgres database for storing the clients' data.
 * flaskapp: a computer program implemented in Flask to perform the tasks over the internet.
 * nginx: web server to handle the HTTP requests. 
 * network: enable communication between the webapp and database containers running on the same daemon host.
 
 After running these 3 commands 
 
```
 docker-compose up -d db
docker-compose run --rm flaskapp /bin/bash -c "cd /opt/services/flaskapp/src && python -c  'import database; database.init_db()'"
```
