```bash
# CREATE VENV
# For linux
virtualenv env -p python3
. env/bin/activate

# For Windows
python -m venv env  
.\env\Scripts\activate

# Install django
pip install django

# Start PROJECT
django-admin startproject disquaire_project

# Install library
pip install psycopg2-binary
pip install django-debug-toolbar

# Run / migrate server
./manage.py runserver
./manage.py migrate

# Start app
django-admin startapp appname
```
