from django.http import HttpResponse
from django.shortcuts import render


def dauletsuper(request):
    return HttpResponse("Dauletsuper")


def home(request):
    return render(request, 'index.html', {'greeting': 'Hello!'})


def button(request):
    user_input = request.GET['user_input']
    lists = [x for x in user_input.split()]
    count = len(lists)
    return render(request, 'reverse.html', {'user_text': user_input, 'word': count})
