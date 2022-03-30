from rest_framework.serializers import ModelSerializer
from Jotters.models import Jotter
from Users.models import User,UserProfile


class JotterSerializer(ModelSerializer):
    class Meta:
        model = Jotter
        fields = ['id','title', 'snippet', 'detail','important']

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email','password1','password2']

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username', 'email','important']
