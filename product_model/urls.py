from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_model_list),
    path('<int:pk>/', views.product_model_detail),
]