### Meta Fetch API

#### Run the app

- Open terminal in *code* directory
- Copy `.env.example` to `.env`
- Run the app `flask run -p 7000`

Access the api at `http://localhost:7000`

### Fetch meta info

```sh
curl --location --request POST 'http://127.0.0.1:7000/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'url=https://mangoradio.stream.laut.fm/mangoradio?t302=2022-05-26_23-02-54&uuid=fce65a34-c18d-4c81-a148-f2b942e06aac'
```
