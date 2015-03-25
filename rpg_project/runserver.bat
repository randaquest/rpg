@echo off
chdir
python manage.py makemigrations
python manage.py migrate
python manage.py syncdb
python populate_rpg.py
python manage.py runserver
pause