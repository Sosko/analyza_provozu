from django.urls import path

from main.views import AboutView, UploadFileView, UploadListView, CarsListView, CarCreateView, CarDetailView, \
    UploadDetailView, UploadParseDetailView, UploadDeleteView, CarDeleteView

urlpatterns = [
    path("", AboutView.as_view(), name='home'),
    # Upload
    path("uploads", UploadListView.as_view(), name="upload_list"),
    path("upload", UploadFileView.as_view(), name='upload_new'),
    path("upload/<slug:pk>", UploadDetailView.as_view(), name='upload'),
    path("upload/<slug:pk>/delete", UploadDeleteView.as_view(), name='upload_delete'),
    path("upload/<slug:pk>/parse", UploadParseDetailView.as_view(), name='upload_parse'),
    # Car
    path("cars", CarsListView.as_view(), name="car_list"),
    path('car', CarCreateView.as_view(), name='car_new'),
    path('car/<slug:pk>', CarDetailView.as_view(), name='car'),
    path("car/<slug:pk>/delete", CarDeleteView.as_view(), name='car_delete'),

]
