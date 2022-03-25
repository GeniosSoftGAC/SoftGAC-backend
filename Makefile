env:
	pipenv shell

setup:
	pip install -r requirements.txt

server:
	cd SoftGAC && python manage.py runserver

gunicorn-test:
	
	cd SoftGAC && gunicorn SoftGAC.wsgi:application --bind localhost:8000

serve-public:
	cd SoftGAC && python manage.py runserver 0.0.0.0:8000

migrations:
	cd SoftGAC && python manage.py makemigrations

migrate:
	cd SoftGAC && python manage.py migrate
