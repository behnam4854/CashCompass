from django.urls import path,include,re_path
from . import views
from django.contrib.admin.views.decorators import staff_member_required


app_name = 'accounts'


urlpatterns =[
    path('dashboard/',views.DashboardView.as_view(),name='dashboard'),
    path("signup/", views.SignupView.as_view(), name="signup"),
]
