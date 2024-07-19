from django.shortcuts import render
from .models import movie_info

# Create your views here.
def creatine(request):
    if request.POST:
        title = request.POST.get('title')
        year = request.POST.get('year')
        movie_obj = movie_info(title=title, year=year)
        movie_obj.save()

    return render(request, 'create.html')


def editer(request):
    return render(request, 'edit.html')


def list(request):
    movie_set=movie_info.objects.all()
    print(movie_set)
    return render(request, 'list.html',{'movies':movie_set})
