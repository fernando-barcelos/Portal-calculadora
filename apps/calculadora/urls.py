
from django.urls import  path
from apps.calculadora.views import index, calcular

urlpatterns = [
    path('', index, name='index'),  # Esta a calculadora que sera chamada como index
    path('calacular/', calcular, name='calcular'),  # Rota para calcular
    #path('historico/', historico, name='historico'),  # Rota
]
