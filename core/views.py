from django.shortcuts import render
from .models import Hymn

def home(request):
    # Placeholder list of hymns
    hymns = Hymn.objects.all()
    return render(request, 'core/home.html', {'hymns': hymns})

def hymn_detail(request, hymn_id):
    # Placeholder hymn details
    hymn = Hymn.objects.get(id=hymn_id)
    if hymn is None:
        return render(request, 'core/hymn_not_found.html', status=404)
    return render(request, 'core/hymn_detail.html', {'hymn': hymn})

def about(request):
    return render(request, 'core/about.html')
