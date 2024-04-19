from django.urls import path
from .views import OrderAPIView,OrderView

urlpatterns = [
    path('',OrderView.as_view()),
    path('create/', OrderAPIView.as_view(), name='create-order'),
]
