# IMDB_BACKEND_DJANGO
This is a simple implementation of an IMDb-like website using Django REST API and Postgres database. This implementation includes the following features:
* Custom user management system.
* Users can create an account, login, and logout.
* Users can search for movies and TV shows.
* Users can view details about movies and TV shows, including their ratings and reviews.
* Users can rate movies and TV shows.
* Users can write reviews for movies and TV shows.
## Installation
1. Clone the repository:
```
git clone https://github.com/karthik-thunga/IMDB_BACKEND_DJANGO.git
```
2. Change into the project directory:
```
cd IMDB_BACKEND_DJANGO
```
3. Create a virtual environment and activate it:
```
python3 -m venv venv
For Linux: source venv/bin/activate
For Windows: venv\Script\activate
```
4. Install the project dependencies:
```
pip install -r requirements.txt
```
5. create .env file and place it in project root directory with following content:
```
DB_ENGINE = django.db.backends.postgresql_psycopg2
DB_NAME = name-of-your-db
DB_USER = name-of-your-user
DB_PASSWORD = password-of-database
DB_HOST = host-of-databse
DB_PORT = port-number-of-db
DEBUG = True
SECRET_KEY = secret-key
```
or if you want to use default database, replace  following code in settings.py file:
```
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}
```
with:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
```
6. Migrate the database:
```
python manage.py migrate
```
7. Run the development server:
```
python manage.py runserver
```
8. The development server should now be running at http://localhost:8000/.

## API Endpoints
The following API endpoints are available:

* api/content/ - List all movies or create a new movie(only admin user).
* api/content/&lt;int:pk&gt;/ - Retrieve, update, or delete a movie by ID.
* api/content/&lt;int:pk&gt;/review/ - List all reviews of a content.
* api/content/&lt;int:pk&gt;/review-create/ - Create review for content.
* api/content/review/&lt;int:pk&gt;/ - Retrieve, update, or delete a review by ID.
* account/login/ - Log in a user.
* account/logout/ - Log out a user.
* account/register/ - Register a new user.
## Authentication
To access the protected API endpoints, users must first authenticate by sending a POST request to the /account/login/ endpoint with a valid username and password. This will return a token, which must be included in the Authorization header of subsequent requests to protected endpoints.

To log out, users can send a POST request to the /account/logout/ endpoint.

To register a new user, users can send a POST request to the /account/register/ endpoint with a username and password.
## Acknowledgements
This project was inspired by the Django REST framework tutorial.


