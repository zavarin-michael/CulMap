from django.shortcuts import render


def home(request):
    return render(request, 'start_page/master.html')
