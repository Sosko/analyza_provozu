from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic import TemplateView


# Create your views here.

def main_html(request):
    return get_template('template.html')

class AboutView(TemplateView):
    template_name = "template.html"