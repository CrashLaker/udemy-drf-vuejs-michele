SHELL=/bin/bash

args := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(args):;@:)

pf=docker-compose run --rm app
admin:
	echo " \
	from django.contrib.auth import get_user_model; \
	User = get_user_model(); \
	User.objects.create_superuser('admin', '', 'admin') \
	" | sed 's/^[ \t]*//g' | $(pf) python manage.py shell

start:
	#python manage.py runserver 0:8000
	docker-compose up -d app

clear:
	find . -type d -name "__pycache__" -prune -exec rm -rf {} \;
	find . -type d -name "migrations" -prune -exec rm -rf {} \;

downup: clear down up admin

down:
	docker-compose down

up:
	#python manage.py runserver 0:8000
	docker-compose up -d

upf:
	#python manage.py runserver 0:8000
	docker-compose up --force -d

build:
	docker-compose build

logs:
	docker-compose logs -f

resetdb:
	docker-compose down db
	docker-compose up -d --force db

m:
	$(pf) python manage.py migrate

mm:
	$(pf) python manage.py makemigrations $(args) 2>&1

mmm: mm m

mm2:
	python manage.py makemigrations
	python manage.py migrate --run-syncdb

app:
	$(pf) sh -c "python manage.py startapp $(args)"

test:
	$(pf) python manage.py test

test2:
	$(pf) sh -c "python manage.py test && flake8"

run:
	$(pf) sh -c "$(args)"

shell:
	$(pf) python manage.py shell

# django-admin startproject app .
# python manage.py startapp products
# Authorization: Token <token>
#

.PHONY: app test m mm mm2 run shell admin start
.ONESHELL:
