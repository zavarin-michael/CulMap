from django.shortcuts import render

from about.forms import CommentForm
from map.models import MapMarks
from django.http import JsonResponse

def map(request):
    if request.method == "GET":
        if request.is_ajax():
            mark = MapMarks.objects.filter(id=request.GET["id"]).values()
            return JsonResponse(mark.first())
        else:
            marks = MapMarks.objects.all().values('id', 'position_x', 'position_y')
            form = CommentForm()
            return render(request, 'map/info-module.html', {"marks": marks, "form": form})
    else:
        form = CommentForm(request.POST)
        a = 1
        marks = MapMarks.objects.all().values('id', 'position_x', 'position_y')
        form = CommentForm()
        return render(request, 'map/info-module.html', {"marks": marks, "form": form})