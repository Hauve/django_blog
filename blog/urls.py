from django.urls import path
from django.conf.urls import static

from . import views
from django.conf import settings

urlpatterns = [
    path('', views.PostView.as_view()),
]