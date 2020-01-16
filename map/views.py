from django.shortcuts import render
from map.models import MapMarks


def map(request):
    marks = MapMarks.objects.all()
    return render(request, 'map/map.html', {"marks": marks})
