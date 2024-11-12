from django.shortcuts import render
from django.http import HttpResponse


def home_page_view(request):
    return HttpResponse("Hello, World!")

def about_page_view(request):  # new
    return render(request, "about.html")
