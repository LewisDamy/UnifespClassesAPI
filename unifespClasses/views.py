from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

from .serializers import SubjectSerializer
from .models import Subject


@api_view(['POST','GET'])  #pass the list of methods allowed in this function
def subject_list(request):
    if request.method == 'GET':
        subject = Subject.objects.all()     # get all the drinks
        serializer = SubjectSerializer(subject, many=True)      # serialize them
        return JsonResponse({"subjects": serializer.data})      # return Json

    if request.method == 'POST':
        serializer = SubjectSerializer(data=request.data)       # create data serializer
        if serializer.is_valid():   # check if the data is valid
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def subject_detail(request, id):
    try:
        serializerSubject = Subject.objects.get(pk=id)      # get from the Subject model the id that was requested
    except Subject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubjectSerializer(serializerSubject)   # pass the subject from models as a serializer format
        return Response(serializer.data)    # return it
    elif request.method == 'PUT':
        serializer = SubjectSerializer(serializerSubject, data=request.data)    # get the data requested as serializer
        if serializer.is_valid():   # check if it's a valid form
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializerSubject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
