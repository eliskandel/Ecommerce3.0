from django.urls import path
from.views import (
    CartItemListView,
    CartItemAddAPIView,
    CartItemRemoveView,
)

urlpatterns = [
    path('',CartItemListView.as_view()),
    path('add/',CartItemAddAPIView.as_view()),
    path('delete/<int:pk>/',CartItemRemoveView.as_view())
]
