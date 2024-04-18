from django.urls import path
from.views import (
    CartItemListView,
    CartItemAddAPIView
)

urlpatterns = [
    path('',CartItemListView.as_view()),
    path('add/',CartItemAddAPIView.as_view())
]
