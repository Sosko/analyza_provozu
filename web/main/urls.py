from django.urls import path

from main.views import main_html, AboutView, UploadFileView

urlpatterns = [
    path("", AboutView.as_view(), name='home'),
    path("upload_file", UploadFileView.as_view(), name='upload_file'),
]
