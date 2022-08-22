# i created this file - Asad
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    print("Hi Asad in django")
    return render(request, 'index.html')
    # return HttpResponse("Hi Asad in django")


def about(request):
    print("Hi Asad in django")
    return HttpResponse("Hi Asad in django about route")


def one(request):
    print("Hi Asad in django")
    return HttpResponse("one.txt")


def removepunc(request):
    return HttpResponse("remove punc")


def capfirst(request):
    return HttpResponse("capitalize first")


def newlineremove(request):
    return HttpResponse("capitalize first")


def spaceremove(request):

    return HttpResponse("space remover")


def charcount(request):

    return HttpResponse("charcount ")
