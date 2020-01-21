from django.shortcuts import render
from map.models import MapMarks


def map(request):
    marks = MapMarks.objects.all()
    if request.method == "GET":
        list1 = request.GET.dict()
        u = -1
        for i in list1:
            u = int(i)
        return render(request, 'map/map.html', {"marks": marks, "id": u})
