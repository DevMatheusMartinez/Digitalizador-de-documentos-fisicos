from django.urls import path
from .views import SelectedFieldAPIView

urlpatterns = [
    path('cursos/', SelectedFieldAPIView.as_view(), name='cursos'),
]