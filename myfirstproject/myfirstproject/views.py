from django.http import HttpResponse
from django.shortcuts import render


def dauletsuper(request):
    return HttpResponse("Dauletsuper")


def home(request):
    return render(request, 'index.html', {'greeting': 'Hello!'})
