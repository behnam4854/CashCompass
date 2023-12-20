from django.urls import path,include,re_path
from . import views
from django.contrib.admin.views.decorators import staff_member_required


app_name = 'intro'


urlpatterns =[
    path('dashboard/',views.home,name='dashboard'),
]
