web: gunicorn movie_basement_api.wsgi:application --log-file - --log-level debug
python movie_basement_api/manage.py collectstatic --noinput
python movie_basement_api/manage.py migrate