# Retailys Django App
- Simple Django REST framework application with Postgres database (db is not needed).
- Django is only here for hosting purpose
- Main goal is working with xml file
- Do 3 things:
  - List number of Products (GET /1)
  - List names of Products (GET /2)
  - List of Products with its spare parts (GET /3)

## How to start application

1. Create and activate virtual environment: `virtualenv venv && source venv/bin/activate`

2. Install requirements: `pip install -r requirements.txt`

3. Create `.env_local_dev` from `.env_local_dev_example` and add all your local properties

4. Start PostgreSQL server, create the database for the project and make sure all database related properties
in the `.env_local_dev` are correct.

5. Or you can use provided DockerFile and docker-compose.yml

## Testing
1. Send GET request on http://127.0.0.1:8000/1 or http://127.0.0.1:8000/2 or http://127.0.0.1:8000/3 based on task you 
would like to app to perform

## Development
- Run `test.sh` before pushing - runs pylint, black, coverage and unit test
