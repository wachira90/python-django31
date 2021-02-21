from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    text = "<h1>index !</h1>" 
    return HttpResponse(text)

def books(request, number):
    text = "<h1>welcome to my app number %s!</h1>"% number
    return HttpResponse(text)

def art(request, year):
    text = "<h1>art  %s </h1>"% year
    return HttpResponse(text)

def comment(request, id):
    text = "<h1>comment  %s </h1>"% id
    return HttpResponse(text)

def hello(request):
    return render(request, "hello.html", {})

def test(request):
    text = "<h1>test !</h1>" 
    return HttpResponse(text)

'''
from django.shortcuts import render

def hello(request):
    return render(request, "\hello.html", {})

------------------------------------

from django.http import HttpResponse

def hello(request):
    text = """<h1>welcome to my app !</h1>"""
    return HttpResponse(text)

------------------------------------

from django.http import HttpResponse

def hello(request, number):
    text = "<h1>welcome to my app number %s!</h1>"% number
    return HttpResponse(text)

'''
