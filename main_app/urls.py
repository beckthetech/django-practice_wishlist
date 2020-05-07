from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('create/', views.wish_create, name='create'),
    path('delete/<int:pk>', views.DeleteWish.as_view(), name='delete')
]
