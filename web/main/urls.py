from django.urls import path

from main.views import main_html, AboutView

urlpatterns = [
    path("", AboutView.as_view()),
]
