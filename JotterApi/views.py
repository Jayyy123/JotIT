from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JotterSerializer,Jotter
from rest_framework import status

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
            'login':'',
            'signup':'',
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

