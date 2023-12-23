#I have created this file-MY SITE
from django.http import HttpResponse


def index(request):
    return HttpResponse('''<h1>WELCOME</h1> <a href="https://youtu.be/uJtoY919sjU?si=8I_-ma4xoWgq3-SV "> mere bhole nath </a> ''')


def about(request):
    return HttpResponse("<h1>WELCOME IN MY WEBSITE </h1>"<a href="about"> back to about </a>)

def firsturl(request):
    return HttpResponse("<h1>WELCOME IN MY WEBSITE first url </h1>")
















