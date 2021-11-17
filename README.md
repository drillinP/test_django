# Project to initiate at Django
Note to run this project 
```bash
# Create a venv
## For linux
virtualenv env -p python3
. env/bin/activate

## For Windows
python -m venv env  
.\env\Scripts\activate

# Install requirements
pip install -r requirements/django.txt

# Run / migrate server
./manage.py migrate
./manage.py runserver
```
