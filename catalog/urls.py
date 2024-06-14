from django.urls import path
from .views import index, details , about




urlpatterns = [
    path('', index, name='index' ),
    path('', details, name='details'),
    path('', about, name='about'),
]

