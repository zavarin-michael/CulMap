from django.shortcuts import render

def home(request):
    return render(request, 'about/about.html')