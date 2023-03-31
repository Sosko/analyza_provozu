from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic import TemplateView, FormView

from main.forms import UploadFileForm
from web.settings import BASE_DIR


# Create your views here.

def main_html(request):
    return get_template('template.html')


class AboutView(TemplateView):
    template_name = "main.html"


def handle_uploaded_file(f):
    with open(BASE_DIR / 'writable' / f.name(), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class UploadFileView(FormView):
    form_class = UploadFileForm
    template_name = 'upload.html'  # Replace with your template.

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/upload_list')
        else:
            return self.form_invalid(form)
