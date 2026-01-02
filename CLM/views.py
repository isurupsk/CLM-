from django.http import HttpResponse


def home(request):
    """Sample Default."""
    return HttpResponse('Hello world')
