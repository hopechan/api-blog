For this project you need poetry and python version 3.8 or higher.

## Getting started

Clone the repository and access the folder apk_monitoring.

```bash
git clone git@github.com:hopechan/api-blog.git
cd api-blog
```

## Create env file
Rename file .env.example to .env

```bash
mv .env.example .env
```

Fill the environment variables with the correct credentials.

## Database
If you are using docker run
```bash
docker exec -i container_name /bin/bash -c "PGPASSWORD=db_password psql -U db_user -d db_name < dump.sql"     
```

otherwise
```bash
psql -U db_user -d db_name < dump.sql
```

## Install dependencies

```bash
poetry install
source .venv/bin/activate
```

## start development site
```bash
flask --app api/v1 run --debug
```