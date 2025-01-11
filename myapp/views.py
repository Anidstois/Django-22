from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Page

def page1_view(request):
    page = Page.objects.get(id=1)
    return render(request, 'page1.html', {'page': page})

def page2_view(request):
    page = Page.objects.get(id=2)
    return render(request, 'page2.html', {'page': page})

def page3_view(request):
    page = Page.objects.get(id=3)
    return render(request, 'page3.html', {'page': page})


@login_required
def admin_only_view(request):
    return render(request, 'admin_only.html', {})