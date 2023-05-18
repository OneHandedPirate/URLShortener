<h1 align="center"> URLShortener </h1>

<p align="center">Simple project to shorten URLs. I used Django, DRF and Celery.</p>

### Requirements:
- Postgresql database
- Redis-server

### Installation:
- Create and activate new virtual environment in the chosen (root) folder. 
- Clone project files to root folder: <br> ```git clone https://github.com/OneHandedPirate/URLShortener.git```
- Install dependencies: <br> ```pip install -r requirements.txt```
- Create `.env` file in the root folder with the following variables:
  
    `DJANGO_SK` - Secret Key for Django Project.
    
    `TZ` - preferred time zone.

    `POSTGRES_USER` - postgres user.
    
    `POSTGRES_PASSWORD` - postgres password.
    
    `POSTGRES_DB` - postgres database.
    
    `POSTGRES_HOST` - postgres host.

    `POSTGRES_PORT` - postgres port.

    `REDIS_HOST` - host of your Redis server.
   
    `REDIS_PORT` - Redis-server post.

    `REDIS_DB` - Redis-server database.

    `TOKEN_LIFETIME` - lifetime of the shortened URLs (in days).
- Apply migrations: <br> ```python manage.py migrate```
- Create superuser : <br> ```python manage.py createsuperuser```

### Start:

- Run Django-server: <br> `python manage.py runserver`
- Run celery worker: <br> `celery -A URLShortener worker -l info`

### Paths description:

  ` ` - main page of the site where you can shorten the URLs.<br>
  `list/` - a list of all shortened URLs. Contains the following info about each URL: original URL, shortened URL, creation time, expiration time (based on `TOKEN_LIFETIME` variable in `.env`) and requests count.<br>
  `api/v1/token_create/` - API endpoint for creating shortened URLs (only POST request available).<br>
  `api/v1/token_list/` - API endpoint for GETing all shortened URLs.
  
