from django.shortcuts import render

from about.forms import CommentForm
from about.models import Comment
from map.models import MapMarks
from django.http import JsonResponse

def Map(request):
    if request.method == "GET":
        if request.is_ajax():
            mark = MapMarks.objects.filter(id = request.GET["id"]).values()
            s = str(mark.first()['id_comment'])

            spis = s.split('_')

            commentslist = []
            for i in spis:
                if (i != ''):
                    a = Comment.objects.filter(id = int(i)).values().first()
                    commentslist.append(a)

            return JsonResponse(mark.first())
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
        mark.id_comment = mark.id_comment + str(data.data["id_mark"]) + '_'
        mark.save()
        comment.save()

        form = CommentForm()
        marks = MapMarks.objects.all().values('id', 'position_x', 'position_y')
        return render(request, 'map/info-module.html', {"marks": marks, "form": form})