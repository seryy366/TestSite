from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    print(request)
    return HttpResponse('hello world')


def test(request):
    print(request)
    return HttpResponse('zzzz')