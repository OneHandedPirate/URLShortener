<h1 align="center"> URLShortener </h1>

<p align="center">Simple project to shorten URLs. I used Django, DRF and Celery.</p>

### Requirements:
- Postgresql database* (optional)
- Redis-server

### Installation:
- Create and activate new virtual environment in the chosen (root) folder. 
- Clone project files to root folder: <br> ```git clone https://github.com/OneHandedPirate/URLShortener.git```
- Install dependencies: <br> ```pip install -r requirements.txt```
- Create `.env` file in the root folder with the following variables:<br>
    `DJANGO_SK` - Secret Key for Django Project.<br>
    `TZ` - preferred time zone.<br>
    `REDIS_HOST` - host of your Redis server.<br>
    `REDIS_PORT` - Redis-server post.<br>
    `REDIS_DB` - Redis-server database.<br>
    `TOKEN_LIFETIME` - lifetime of the shortened URLs (in days).<br>
 
- Apply migrations: <br> ```python manage.py migrate```
- Create superuser : <br> ```python manage.py createsuperuser```


*If you chose Postgresql as your database  - perform the followings steps:<br>  
  - Uncomment respective lines of code in `DATABASES` section in `URLShortener/settings.py` and comment or simply delete config for sqlite3.
  - Add the following variables in `.env`:<br>
    `POSTGRES_USER` - postgres user.<br>
    `POSTGRES_PASSWORD` - postgres password.<br>
    `POSTGRES_DB` - postgres database.<br>
    `POSTGRES_HOST` - postgres host.<br>
    `POSTGRES_PORT` - postgres port.<br>
  - Install `psycopg2`:<br>
    `pip install psycopg2` (Windows)<br>
    `pip install psycopg2-binary` (Linux or MasOS)
### Start:

- Run Django-server: <br> `python manage.py runserver`
- Run celery worker: <br> `celery -A URLShortener worker -l info`

### Paths description:

  ` ` - main page of the site where you can shorten the URLs.<br>
  `list/` - a list of all shortened URLs. Contains the following info about each URL: original URL, shortened URL, creation time, expiration time (based on `TOKEN_LIFETIME` variable in `.env`) and requests count.<br>
  `api/v1/token_create/` - API endpoint for creating shortened URLs (only POST request available).<br>
  `api/v1/token_list/` - API endpoint for GETing all shortened URLs with detailed information (50 URLs on each page by default, you can change this number in URLShortener/settings.py, in  `DRF Config` section).
  
