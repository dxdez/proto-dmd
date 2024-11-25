# Proto DMD - Django Markdown

> **Note: This project is no longer actively maintained. It has been archived for historical purposes. Feel free to explore the code, but please note that it is no longer in use or supported.**

This application is a prototype written in Django for rendering markdown files. 

### Running Application in Docker

The application runs within a docker container. See the official documentation for docker to set it up on your system [here](https://docs.docker.com/engine/install/ "here").

In order to allow the client to render, make sure the host is allowed within the application. This is done by modifying the `proto_dmd_project/settings.py` file like so (development only):
`````
ALLOWED_HOSTS = ['*']
`````

Execute the following command to run the application:
`````
docker compose up -d
`````

The application will be available on PORT 8000, in browser use the host address:port to view the application:
`````
<hostname>:8000
`````

Execute the following command to shutdown:
`````
docker compose down -v
`````
