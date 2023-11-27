from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.


def index(request):
    # SELECT * FROM movies_movie
    movies = Movie.objects.all()
    # SELECT * FROM mvies_movie WHERE ...
    # Movie.objects.filter(release_year=1984)
    # Movie.objects.get(id=1)

    # output = ', '.join([m.title for m in movies])
    # return HttpResponse(output)

    return render(request, '../templates/index.html', {'movies': movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, '../templates/detail.html', {'movie': movie})
