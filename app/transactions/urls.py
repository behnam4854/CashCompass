from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    path('plot/', views.plot_view, name='plot_view'),

    # path('plot-view/', views.plot_view, name='plot'),
    # path('report-view/', views.report_view, name='reporyt'),
]
