# Proto DMD - Django Markdown

This application is a prototype written in Django for rendering markdown files. Markdown is a plain text formatting language that can automatically convert to HTML for publishing on the Web. Due to its accessible syntax and widespread use in static site generators, productivity apps, and content management tools, it’s become a popular alternative to rich-text editors for both technical and non-technical content creators.

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

Execute the following command to shutdown:
`````
docker compose down -v
`````
