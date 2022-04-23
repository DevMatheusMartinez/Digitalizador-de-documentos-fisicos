from django.urls import path
from .views import SelectedFieldAPIView, ScanningApiView

urlpatterns = [
    path('digitalizar/', ScanningApiView.as_view(), name='digitalizar'),
    path('campos/', SelectedFieldAPIView.as_view(), name="campos")
]