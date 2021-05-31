from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('',views.index,name='order'),
    path('show/',views.show,name='show'),
    path('update/<int:pk>',updateOrder.as_view(),name='update'),
    path('delete/<int:pk>',deleteOrder.as_view(),name='delete'),
]