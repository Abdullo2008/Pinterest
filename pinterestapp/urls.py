from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('about-me', about, name='about'),
    path('search', SearchView, name='search'),
    path('image/<int:id>', SingleView, name='single'),
    path('add', add.as_view(), name='add'),
    path('delete/<int:pk>/', delete.as_view(), name='delete'),
]
