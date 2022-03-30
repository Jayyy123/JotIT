from socket import send_fds
from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile


@receiver(post_save,sender=User)
def CreateProfile(instance,created,sender,**kwargs):
    if created:
        user = instance
        user_profile = UserProfile.objects.create(
            owner = user,
            first_name = user.first_name,
            last_name = user.last_name,
            username = user.username,
            email = user.email
        )

@receiver(post_delete,sender=UserProfile)
def DeleteUser(sender,instance,**kwargs):
    instance.delete