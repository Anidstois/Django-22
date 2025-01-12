from django.template.defaulttags import lorem
from django.urls import path
from . import views  #

urlpatterns = [
    # Примеры вложенных маршрутов, если они есть
    path('page1/', views.page1_view, name='page1'),
    path('page2/', views.page2_view, name='page2'),
    path('page3/', views.page3_view, name='page3'),
]
