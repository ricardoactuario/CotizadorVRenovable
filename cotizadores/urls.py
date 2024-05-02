from django.urls import path
from . import views


urlpatterns = [
    path('SeguroTemporalAnualRenovable/', views.CotizadorTAR),
]