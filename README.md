# Calorie-Counter

1.) created virtual enviornment using command
mkvirtualenv myvenv

2.)install requiremnets.txt file
pip install -r requirements.txt
 
3.)activated virtual enviornment using command
myvenv\Scripts\activate

4.) Created django project using command
django-admin.exe starproject caloriecounter .


5.) Created django app using command
django-admin.exe startapp mainapp

6.)create admin/superuser
python manage.py createsuperuser

enter username and password

admin
admin@123

7.)run project
python manage.py runserver
