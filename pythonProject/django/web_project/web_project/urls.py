from django.urls import path
from django.web import views

urlpattern=[
    path('page1',views.home,name='home'),
    path('page2/',views.secondpage,name='secondpage')
]