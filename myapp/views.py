from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.flatpages.models import FlatPage

def page1_view(request):
    flatpage = FlatPage.objects.get(url='/page1/')
    return render(request, 'myapp/page1.html', {'flatpage': flatpage})

def page2_view(request):
    flatpage = FlatPage.objects.get(url='/page2/')
    return render(request, 'myapp/page2.html', {'flatpage': flatpage})

def page3_view(request):
    flatpage = FlatPage.objects.get(url='/page3/')
    return render(request, 'myapp/page3.html', {'flatpage': flatpage})


@login_required
def admin_only_view(request):
    return render(request, 'admin_only.html', {})