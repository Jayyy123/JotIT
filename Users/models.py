from django.db import models
from django.contrib.auth.models import User
import uuid


class UserProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name =  models.CharField(max_length=200,default='user', blank=False,null=False)
    last_name = models.CharField(max_length=100, default='user', blank=False,null=False)
    username = models.CharField(max_length=100, default='user', blank=False,null=False)
    email = models.EmailField(blank=False,null=False, default='user@email.com')
    stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)


    def __str__(self) -> str:
        return self.username
