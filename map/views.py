from django.shortcuts import render
from map.models import MapMarks
from django.http import JsonResponse

def map(request):
    if request.method == "GET":
        if request.is_ajax():
            mark = MapMarks.objects.filter(id=request.GET["id"]).values()
            return JsonResponse(mark.first())
        else:
            marks = MapMarks.objects.all().values('id', 'position_x', 'position_y')
            return render(request, 'map/map.html', {"marks": marks})
