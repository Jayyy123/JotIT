from pyexpat import model
from .models import UserProfile,User
from  django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email', 'password1', 'password2']

class UserProfileform(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name','username','email']

