from django.shortcuts import render

from about.forms import CommentForm
from about.models import Comment
from map.models import MapMarks
from django.http import JsonResponse

def Map(request):
    if request.method == "GET":
        if request.is_ajax():
            if request.GET["type"] == '1':
                mark = MapMarks.objects.filter(id = request.GET["id"]).values()
                return JsonResponse(mark.first())
            else:
                comment = Comment.objects.filter(id = request.GET["id"]).values()
                return JsonResponse(comment.first())
        else:
            marks = MapMarks.objects.all().values('id', 'position_x', 'position_y')
            form = CommentForm()
            return render(request, 'map/info-module.html', {"marks": marks, "form": form})
    else:
        data = CommentForm(request.POST)
        comment = Comment()
        comment.comment = data.data["comment"]
        comment.username = data.data["username"]
        comment.id_mark = data.data["id_mark"]
        mark = MapMarks.objects.get(id = data.data["id_mark"])
        comment.save()
        mark.id_comment = mark.id_comment + str(comment.id) + '_'
        mark.save()

        form = CommentForm()
        marks = MapMarks.objects.all().values('id', 'position_x', 'position_y')
        return render(request, 'map/info-module.html', {"marks": marks, "form": form})