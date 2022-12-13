from django.urls import path
from aggregator import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.user_login, name='user_login')
]