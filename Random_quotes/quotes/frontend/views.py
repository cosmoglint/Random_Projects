from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def random_joke(request):
    ctx = {
        'texts': ["hi", "hello"]
    }
    return render(request, 'frontend/index.html', ctx)
