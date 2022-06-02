from django.contrib import admin
from django.urls import path

from tenant import views


urlpatterns = [
    path('our_team/', views.our_team, name='team'),
    path('admin/', admin.site.urls),
]
