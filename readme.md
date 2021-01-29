Django Blog App
===
## Install
        pip install -r requirements.txt
        python manage.py migrate

## Run local
        python manage.py runserver

## Docker
        sudo docker build -t django-blog . 
        sudo docker run -p 8000:8000 django-blog 