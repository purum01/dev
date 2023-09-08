from django.db import models
from django.conf import settings
from django.core.mail import send_mail 
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)


def on_send_mail(sender, **kwargs):
    if kwargs['created'] :
        user = kwargs['instance']
        send_mail('가입인사','가입을 환영합니다.', 'admin@sky.com', [user.email], fail_silently=False)
        

post_save.connect(on_send_mail, sender=settings.AUTH_USER_MODEL)


from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.signals import user_logged_in

class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

def block_duplicate_login(sender, request, user, **kwargs):
    login_user_list = UserSession.objects.filter(user=user)
    
    for user_session in login_user_list:
        session = SessionStore(user_session.session_key)
        # session.delete()
        session['blocked'] = True
        session.save()
    
    session_key = request.session.session_key
    UserSession.objects.create(user=user, session_key = session_key)

user_logged_in.connect(block_duplicate_login)