from django.shortcuts import render, get_object_or_404
from .models import Movie

from django.db.models import Q

from django.http import HttpResponseRedirect, HttpResponse
import json

# Create your views here.
def homepage(request):
    context = {
        'var1': 'This is to handle input',
        'current_email': 'Not defined'
    }
    return render(request, 'homepage.html', context)


def movie_list(request):
    movies = Movie.objects.all()
    data = [{'name': movie.name, 'year': movie.year, 'genre': movie.genre} for movie in movies]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json')


def movie_detail(request):
    movie_name = request.GET.get('movie_name')
    movie = get_object_or_404(Movie, name=movie_name)
    data = {'name': movie.name, 'year': movie.year, 'genre': movie.genre}
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json')