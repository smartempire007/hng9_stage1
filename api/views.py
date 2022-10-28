from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def hng9Stage1(request):
    profile = {"slackUsername": "smartempire007", "backend": True, "age": 31, "bio": "I'm Nwadike Joseph ex julius berger Nigeria PLC mechanical engineer that's trying to transition to tech industry"}
    return JsonResponse(profile)
