from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JotterSerializer,Jotter,UserSerializer
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken


    # links = {
    #     'users':{
    #         'login':'http://127.0.0.1:8000/users/',
    #         'signup':'http://127.0.0.1:8000/users/signup',
    #         'logout':'http://127.0.0.1:8000/users/logout',
    #         'profile':'http://127.0.0.1:8000/users/profile/',
    #         'createProfile':'',
    #         'editProfile':'',
    #         'deleteProfile':'',
    #     },
    #     'jotters':{
    #         'allJotters':'http://127.0.0.1:8000/jotters/',
    #         'jotter':'',
    #         'addJotter':'http://127.0.0.1:8000/jotters/add_jotter/',
    #         'deleteJotter':'',
    #         'editJotter':'http://127.0.0.1:8000/jotters/edit_jotter/id',
    #     }
    # }

@api_view(['GET'])
def api_overview(request):
    
    links = {
        'all links': 'http://127.0.0.1:8000/jotterapi/v1/',
        'users':{
            'login':'http://127.0.0.1:8000/jotterapi/v1/user-login/',
            'signup':'http://127.0.0.1:8000/userapi/v1/signup/',
            'logout':'',
            'profile':'',
            'createProfile':'',
            'editProfile':'',
            'deleteProfile':'',
        },
        'jotters':{
            'allJotters':'http://127.0.0.1:8000/jotterapi/v1/jotters/',
            'jotter':'http://127.0.0.1:8000/jotterapi/v1/jotter/<str:pk>/',
            'addJotter':'http://127.0.0.1:8000/jotterapi/v1/add-jotter/',
            'editJotter':'http://127.0.0.1:8000/jotterapi/v1/edit-jotter/',
            'deleteJotter':'http://127.0.0.1:8000/jotterapi/v1/delete-jotter/<str:pk>/',
        }
    }

    return Response(links)

@api_view(['GET'])
def jotters(request):
    jott = Jotter.objects.all()
    serializer = JotterSerializer(data=jott,many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def jotter(request,pk):
    jott = Jotter.objects.get(id=pk)
    serializer = JotterSerializer(jott,many=False)

    return Response(serializer.data)

@api_view(['POST'])
def add_jotter(request):
    if request.method == 'POST':
        serializer = JotterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def edit_jotter(request,pk):
    jott = Jotter.objects.get(id=pk)
    serializer = JotterSerializer(instance=jott, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def delete_jotter(request,pk):
    jott = Jotter.objects.get(id=pk)
    if request.method == 'DELETE':
        jott.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)

# User Api

@api_view(['POST'])
def user_login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _,token = AuthToken.objects.create(user)

    return Response({
        'user_info': {
            'id': user.id,
            'username':user.username,
            'firstname':user.first_name,
            'lastname':user.last_name,
            'email': user.email,
        },
        'token': token
    })

@api_view(['GET'])
def get_user(request):
    user = request.user

    if user.is_authenticated:
        return Response({
            "user_info":{
                "id":user.id,
                "username":user.username,
                "first_name":user.first_name,
                "last_name":user.last_name,
                "email":user.email
            }
        })
    
    return Response({"error":"you do not have access to this account"},status=400)


@api_view(['POST'])
def user_signup(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()

    _,token = AuthToken.objects.create(user)

    return Response({
        'user_info': {
            'id': user.id,
            'username':user.username,
            'firstname':user.first_name,
            'lastname':user.last_name,
            'email': user.email,
            'pass':user.password
        },
        'token': token
    })
