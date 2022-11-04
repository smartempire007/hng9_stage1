from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from . import serializer


@api_view(['GET'])
def hng9Stage1(request):
    profile = {"slackUsername": "smartempire007", "backend": True, "age": 31, "bio": "I'm Nwadike Joseph ex julius berger Nigeria PLC mechanical engineer that's trying to transition to tech industry"}
    return JsonResponse(profile)


class Operations:
    
    def addition(x, y):
        return x + y

    def subtraction(x, y):
        return x - y

    def multiplication(x, y):
        return x * y
    
    
@api_view(['GET', 'POST'])
def mathFunc(request, format=None):
    if request.method == 'GET':
        data = {"slackUsername": "smartempire007", "backend": True, "age": 31, "bio": "I'm Nwadike Joseph ex julius berger Nigeria PLC mechanical engineer that's trying to transition to tech industry"}
        return Response(data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serialized_data = serializer.MathematicSerializer(data=request.data)
        if serialized_data.is_valid():
            print(serialized_data.data)
            if serialized_data.data['operation_type'] == 'MULTIPLICATION':
                data = {
                    "slackUsername": "smartempire007",
                    "result": Operations.multiplication(serialized_data.data['x'], serialized_data.data['y']),
                    "operation_type": 'multiplication'
                },
                return Response(data, status=status.HTTP_201_CREATED)
        
            if serialized_data.data['operation_type'] == 'ADDITION':
                data = {
                    "slackUsername": "smartempire007",
                    "result": Operations.addition(serialized_data.data['x'], serialized_data.data['y']),
                    "operation_type": 'addition'
                }
                return Response(data, status=status.HTTP_201_CREATED)
        
            if serialized_data.data['operation_type'] == 'SUBTRACTION':
                data = {
                    "slackUsername": "smartempire007",
                    "result": Operations.subtraction(serialized_data.data['x'], serialized_data.data['y']),
                    "operation_type": 'subtraction'
                }
                return Response(data, status=status.HTTP_201_CREATED)
            serialized_data.save()
        return Response(data=serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    