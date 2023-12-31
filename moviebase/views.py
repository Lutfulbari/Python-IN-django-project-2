from django.shortcuts import render
from moviebase.models import Movie,Actor,Director

# Create your views here.

def home(request):
    all_movies = Movie.objects.all()
    return render(request,"home.html",{'movies':all_movies})

def oneMovie(request,key):
    movie = Movie.objects.get(pk=key)
    date = str(movie.r_date)
    return render(request,"onemovie.html",{'movie':movie,'date':date})

def oneActor(request,key):
    actor = Actor.objects.get(pk=key)
    date = str(actor.b_date)
    return render(request,"oneactor.html",{'actor':actor,'date':date})