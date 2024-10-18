### Meta Fetch API

#### Run the app

- Create virtualenv using `python -m venv .venv`
- Activate virtualenv
- Install requirements `pip install -r requirements.txt`
- Copy `.env.example` to `.env`
- Run the app `flask run -p 8000`

Access the api at `http://127.0.0.1:8000`

#### Run the app using Docker

- Install Docker on your machine
- Open the folder in your terminal
- Build the image `docker build -t meta .`
- Run the a container `docker run -d -p 8000:8000 meta`

Access the api at `http://127.0.0.1:8000`

### Fetch meta info

```sh
curl --location --request POST 'http://127.0.0.1:8000/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'url=https://mangoradio.stream.laut.fm/mangoradio?t302=2022-05-26_23-02-54&uuid=fce65a34-c18d-4c81-a148-f2b942e06aac'
```
