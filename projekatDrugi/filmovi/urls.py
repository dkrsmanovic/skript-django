from django.contrib import admin
from django.urls import path

from . import views

app_name = 'film'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listaFilmova, name="lista"),

    path('create/', views.createMovie, name="create"),
    path('update/<int:film_id>/', views.updateMovie, name="update"),
    path('delete/<int:film_id>/', views.deleteMovie, name="delete")
]
