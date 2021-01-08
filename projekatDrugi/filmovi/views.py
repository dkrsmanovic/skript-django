from django.shortcuts import render, redirect

from .forms import KreirajFilm
from .models import Film
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def listaFilmova(request):
    lista = Film.objects.all().order_by('godina')
    return render(request, 'filmovi/lista.html', {'lista': lista})

@login_required(login_url="/accounts/login/")
def createMovie(request):
    if request.method == 'POST':
        form = forms.KreirajFilm(request.POST)
        if form.is_valid():
            #sacuvaj
            instance = form.save(commit=False)
            instance.kreiraoJe = request.user
            instance.save()
            return redirect('film:lista')
    else:
        form = forms.KreirajFilm()
    return render(request, 'filmovi/create.html', {'form': form })

@login_required(login_url="/accounts/login/")
def updateMovie(request, film_id):
    film = Film.objects.get(id = film_id)
    form = KreirajFilm(instance = film)
    if request.method == 'POST':
        form = KreirajFilm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return redirect('film:lista')
        else:
            print(ValueError)
    return render(request, 'filmovi/update.html', {'form': form, 'film_id': film_id })

@login_required(login_url="/accounts/login/")
def deleteMovie(request, film_id):
    film = Film.objects.get(id=film_id)

    if request.method == 'POST':
        film.delete()
        return redirect('film:lista')

    return render(request, 'filmovi/delete.html', {'form': film, 'film_id': film_id})