from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from tenant import views

def home(request):
    return HttpResponse('<h1>Hello World</h1>')

urlpatterns = [
    path('', home),
    path('our_team/', views.our_team, name='team'),
    path('admin/', admin.site.urls),
]
