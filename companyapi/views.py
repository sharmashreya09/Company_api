
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
def home_page(request):

    return HttpResponse("<h1>COMPANY AND EMPLOYEE API<h1>")