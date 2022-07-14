# Welcome to the Anythink Market repo

To start the app use Docker. It will start both frontend and backend, including all the relevant dependencies, and the db.

Please find more info about each part in the relevant Readme file ([frontend](frontend/readme.md) and [backend](backend/README.md)).

## Development

When implementing a new feature or fixing a bug, please create a new pull request against `main` from a feature/bug branch and add `@vanessa-cooper` as reviewer.

## First setup
### Install Docker
To install Docker follow this [link](https://docs.docker.com/get-docker/).
Then, you can verify if the docker is installed correctly using in the terminal the following commands
```
docker -v
docker-compose -v
```
Now you can run the project from the root directory using ```docker-compose up```

Links to try the web service:
[http://localhost:3000/docs](http://localhost:3000/docs)
[http://localhost:3000/api/ping](http://localhost:3000/api/ping)
[http://localhost:3001/register](http://localhost:3001/register)

** To enter inside of the container you can run ```docker exec``` command








