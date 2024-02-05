from django.urls import path
from . import views


app_name = 'budgest'


urlpatterns =[
    path('addmoney/',views.AddMoneyView.as_view(),name='add-money'),
]
