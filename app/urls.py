from django.urls import path
from .views import SelectedFieldAPIView, ScanningApiView, ConnectionsMysqlApiView

urlpatterns = [
    path('pegar-valores/', ScanningApiView.as_view(), name='pegar-valores'),
    path('campos/', SelectedFieldAPIView.as_view(), name="campos"),
    path('connections-mysql/', ConnectionsMysqlApiView.as_view(), name="connection-mysql")

]