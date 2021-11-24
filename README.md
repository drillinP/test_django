# Project to initiate at Django
To initiate at Django I use the tutorial from [OpenClassroom](https://openclassrooms.com/fr/courses/4425076-decouvrez-le-framework-django)
* Note to run this project 
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

# Run tests
python ./manage.py test
```
