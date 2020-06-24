from django.shortcuts import render

from about.forms import CommentForm
from about.models import Comment
from map.forms import MarkForm
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
            form_comment = CommentForm()
            form_mark = MarkForm()
            return render(request, 'adding-mark/adding-mark.html', {"marks": marks, "form_comment": form_comment, "form_mark": form_mark})
    else:
        data = CommentForm(request.POST)
        if (data.data["type"] == '1'):
            comment = Comment()
            comment.comment = data.data["comment"]
            comment.username = data.data["username"]
            comment.id_mark = data.data["id_mark"]
            mark = MapMarks.objects.get(id = data.data["id_mark"])
            comment.save()
            mark.id_comment = mark.id_comment + str(comment.id) + '_'
            mark.save()
        else:
            mark = MapMarks()
            mark.comment = data.data["comment"]
            mark.name = data.data["name"]
            mark.image = data.data["image"]
            mark.position_y = float(data.data["position_y"])
            mark.position_x = float(data.data["position_x"])
            mark.save()
        form = CommentForm()
        form_mark = MarkForm()
        marks = MapMarks.objects.all().values('id', 'position_x', 'position_y')
        return render(request, 'adding-mark/adding-mark.html', {"marks": marks, "form": form, "form_mark": form_mark})