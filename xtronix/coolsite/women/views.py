from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

def index(request): #  HttpRequest
    return HttpResponse('Страница приложения women')



def categories(request, catid): #  HttpRequest
    if request.GET:
        print(request.GET) 
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')


def archive(request, year):
    if int(year) > 2023:
        return redirect('home', permanent=True) 
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Cтраница не найдена!</h1>') 
