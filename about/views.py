from django.shortcuts import render

from about.forms import CommentForm

def home(request):
    if request.method == 'POST':
        ass=1
    else:
        form = CommentForm()
        return render(request, 'about/about.html', {'form': form})
