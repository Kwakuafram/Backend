import json
from django.http import JsonResponse

# Create your views here.
def home(request):
    return JsonResponse( { "slackUsername": "Richmond Forkuo Afram", "backend": "True", "age": "25", "bio": "i have the grit of becoming a backend developer" })
