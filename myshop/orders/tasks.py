#python manage.py shell

from django.core.mail import send_mail
send_mail("subject","msg",'from_email@test.com',["to_email@test.com"])