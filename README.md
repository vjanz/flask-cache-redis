# Flask-cache-redis

## Installation & Usage

To use this project, start by cloning the repository:
```bash
git clone https://github.com/vjanz/flask-cache-redis.git
```
cd into the project, and make a copy of `.env_example` to `.env`
```bash
$ cp .env_example .env
```

### Build and run the stack
You can run the application stack (Flask application and Redis) with Docker, respectively docker-compose. 
```docker
docker-compose up -d --build
```

#### Remove the stack
```docker
docker-compose down -v
```

### Test the application (API)
We can use `curl` to make requests to our API. There is one endpoint `/universities`, so let's test that out.

```curl
curl localhost:5000/universities?country=Germany
```

### License
This project is licensed under the terms of the MIT license.
