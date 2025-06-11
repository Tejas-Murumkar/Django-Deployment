from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Film

# Create your views here.
def index(request):
    return HttpResponse(render(request, "index.html"))

def films(request):
    films = Film.objects.all()
    films = films.order_by("-rating")
    print(films[0].name)
    return HttpResponse(render(request, "films.html", {"films": films}))