# Psychology

Psychology is a service built with Django for its ORM, and FastAPI + Strawberry for its interfaces.
This is a Docker

In order for the project correctly work, please consider you to use::

- Docker version >= 23.0.5, build bc4487a
- Docker Compose >= version v2.17.3

# Installation

1. First, clone this repository:

```bash
git clone https://github.com/monioalmagro/decires.git
```

2. Copy the environment vars:

```bash
cp .env.dist .env
```

## Environment variables

| Variable                  | Description                                                                          | required |
| ------------------------- | ------------------------------------------------------------------------------------ | -------- |
| DATABASE_URL              | Principal Project BD                                                                 | true     |
| DJANGO_SETTINGS_MODULE    | The location of the base settings                                                    | true     |
| ENVIROMENT_FILENAME       | Name of the file containing the environment variables, defined as `.env` by default. | true     |
| DEBUG                     | Define values to settings DEBUG                                                      | true     |
| SECRET_KEY                | Define values to settings SECRET_KEY                                                 | true     |
| DECIRES_EMAIL             | Define values to settings DECIRES_EMAIL                                              | true     |
| DECIRES_URL               | Define values to settings DECIRES_URL                                                | true     |
| DJANGO_ALLOW_ASYNC_UNSAFE | Define values to settings DJANGO_ALLOW_ASYNC_UNSAFE                                  | true     |

3. Init project:

```bash
make init
```

4. Show containers:

```bash
make ps
```

This results in the following running containers:

```bash
docker-compose ps
NAME                  IMAGE               COMMAND                  SERVICE             CREATED             STATUS              PORTS
psychology_api        psychology-api      "/bin/sh -c 'python …"   api                 23 minutes ago      Up 23 minutes       0.0.0.0:9000->9000/tcp
psychology_postgres   postgres:latest     "docker-entrypoint.s…"   postgres            23 minutes ago      Up 23 minutes       0.0.0.0:5432->5432/tcp
psychology_web        psychology-web      "bash -c 'python3 ma…"   web                 23 minutes ago      Up 23 minutes       0.0.0.0:8000->8000/tcp
```

The microservices are running at:

- API: [http://localhost:9000/api/graph/psychology/](http://localhost:9000/api/graph/psychology/)
- Admin: [http://localhost:8000/admin](http://localhost:8000/admin/)

5. Run the linters:

```bash
make lint
```

6. Managing dependencies with Poetry:

```bash
### To add
docker-compose run --rm api poetry add <dependenciy_name>

### To remove
docker-compose run --rm api poetry remove <dependenciy_name>
```
