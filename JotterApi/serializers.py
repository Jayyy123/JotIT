from rest_framework import validators
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
        fields = ['first_name', 'last_name', 'username', 'email','password']

        extra_kwargs = {
            "password": {"write_only" : True},
            "email": {
                'required':True,
                'allow_blank':False,
                'validators':[
                    validators.UniqueValidator(
                        User.objects.all(),"A user with that email already exists"
                    )
                ]
            }
        }
    def create(self,validated_data):

        username = validated_data.get('username')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        email = validated_data.get('email')
        password = validated_data.get('password')

        user = User.objects.create(
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
            email = email,
        )

        return user

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username', 'email','important']
