import requests
from .models import Url
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required()
def base_view(request):
    urls = Url.objects.order_by('id')
    return render(request, 'url/base.html', {'urls': urls})

@login_required()
def url_status_code(request, id):
    url = Url.objects.get(id=id)
    try:
        path = requests.get(url.path)
        code = path.status_code
    except Exception:
        code = "This site can't be reached"

    return HttpResponse(code)