echo 'SET A SECRET KEY BEFORE RUNNING'
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
