# prowessive-service

prowessive service

## Prepare virtual environment

```bash 
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Start database

```bash
docker-compose up -d
``` 

## Run service

```bash 
uvicorn main:app --reload
``` 

## Execute functional tests

```bash
pytest -s
``` 



## Access to the service info

Open link below with your web browser:

[http://localhost:8000/docs](http://localhost:8000/docs)