.PHONY: allcommands

git:
	git add .
	git commit -m "Building a Complete Django Application"
	git push


migrate:
	python manage.py makemigrations
	python manage.py migrate

server:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver

