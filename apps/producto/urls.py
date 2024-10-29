from django.urls import path
from apps.producto.views import ProductoView
urlpatterns = [
    path('productos/',ProductoView.as_view()),
]