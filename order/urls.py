from django.urls import path
from .views import OrderAPIView

urlpatterns = [
    path('create/', OrderAPIView.as_view(), name='create-order'),
]
