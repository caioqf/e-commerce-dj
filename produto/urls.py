from django.urls import path
from . import views


app_name = 'detalhe_produto'

urlpatterns = [
    path('produto/', views.produto, name='produto')
]
