from django.urls import path
from .views import ProductoView, ProductoDetallesView
urlpatterns = [
    path('productos/',ProductoView.as_view(),name='producto'),
    path('producto_detalles/<int:pk>',ProductoDetallesView.as_view(),name='producto_detalles')
]