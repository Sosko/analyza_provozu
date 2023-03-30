from django.http import HttpResponse


def static_file(request):
    with open("static/swagger.json", "r") as f:
        return HttpResponse(f.read(), content_type="text/plain")
