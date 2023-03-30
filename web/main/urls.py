from django.urls import path

from main.views import main_html

urlpatterns = [
    path("", main_html),
]
