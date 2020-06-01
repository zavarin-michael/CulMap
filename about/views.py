from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        ass=1
    else:
        return render(request, 'about/about.html')
