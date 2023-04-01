import csv
import re
from logging import error

from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template.defaulttags import url
from django.urls import reverse
from django.views.generic import TemplateView, FormView, ListView, DetailView, CreateView, DeleteView

from main.forms import UploadFileForm
from main.functions import prepare_parse
from main.models import Uploads, Cars, Positions
from web.settings import BASE_DIR


# Create your views here.

class AboutView(TemplateView):
    template_name = "main.html"


def handle_uploaded_file(f):
    with open(BASE_DIR / 'writable' / f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class UploadFileView(FormView):
    form_class = UploadFileForm
    template_name = 'upload.html'  # Replace with your template.

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            u = Uploads(name=request.FILES['file'].name, car=Cars(id=request.POST['car']))
            u.save()
            return redirect('upload', pk=u.id)

        else:
            return self.form_invalid(form)


class UploadListView(ListView):
    template_name = 'upload_list.html'
    model = Uploads


class UploadDetailView(DetailView):
    model = Uploads
    template_name = 'upload_view.html'


class UploadDeleteView(DeleteView):
    model = Uploads
    success_url = "/upload_list"
    template_name = "upload_confirm_delete.html"


class UploadParseDetailView(DetailView):
    model = Uploads
    template_name = 'upload_parse.html'

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(UploadParseDetailView, self).get_context_data(**kwargs)
        file = BASE_DIR / 'writable' / context['object'].name
        data = prepare_parse(file_with_path=file)
        if not re.match(r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}.\d+', data['time'][0]):
            if re.match(r'^\d{4}-\d{2}-\d{2}.*', context['object'].name):
                holder = context['object'].name[0:10] + " "
            else:

                holder = "2000-01-01 "
        else:
            holder = ""
        for position in data["position"]:
            if not position[1] or not position[2]:
                continue
            Positions(
                car=context['object'].car,
                date=holder + position[0],
                latitude=position[1],
                longitude=position[2],
            ).save()
        context['data'] = data
        return context


class CarsListView(ListView):
    model = Cars
    template_name = 'cars_list.html'


class CarCreateView(CreateView):
    model = Cars
    template_name = 'cars_new.html'
    fields = [
        'name',
        'description'
    ]


class CarDetailView(DetailView):
    model = Cars
    template_name = 'cars_view.html'


class CarDeleteView(DeleteView):
    model = Cars
    success_url = "/cars"
    template_name = "cars_confirm_delete.html"
