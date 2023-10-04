from django.urls import path
from .views import BookList, add,remove,show
urlpatterns = [
    path('', BookList.as_view(), name='list'),
    path('add/', add, name='shopping-cart-add'),
    path('remove/', remove, name='shopping-cart-remove'),
    path('show/', show, name='shopping-cart-show'),
]
