```bash
virtualenv env -p python3
. env/bin/activate
pip install django
django-admin startproject disquaire_project
pip install psycopg2-binary

./manage.py runserver
./manage.py migrate

pip install django-debug-toolbar

django-admin startapp appname
```
