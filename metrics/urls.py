from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start_at=<str:start_at>&end_at=<str:end_at>', views.MetricsList.as_view(), name='metrics'),
    path('correlation/start_at=<str:start_at>&end_at=<str:end_at>&symbols=<str:symbols>', views.Correlation.as_view(),
         name='correlation')
]
