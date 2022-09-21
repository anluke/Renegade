from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<product_id>', views.product_info, name='product_info'),
]