import requests
from .models import Url
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.



@login_required()
def url_list(request):
    urls = Url.objects.order_by('id')
    for url in urls:
        try:
            path = requests.get(url.path)
            url.code = path.status_code
        except Exception:
            url.code = "This site can't be reached"

    return render(request, 'url/url_list.html', {'urls': urls})

@login_required()
def base_view(request):
    return render(request, 'url/base.html', {})