from django.urls import path
from . import views
from .views import OrderListCreateView, OrderRetrieveAPIView, UserProfileListCreateView, UserProfileRetrieveView,login_view, logout_view

urlpatterns = [
    path("", views.register, name="register"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # Страница регистрации
    path("home/", views.home, name="index"),# Главная страница теперь по "/"
    path('g63/', views.g63, name='g63'),
    path('e63/', views.e63, name='e63'),
    path('gle/', views.gle, name='gle'),
    path('S_Class/', views.S_Class, name='S_Class'),
    path('order/', views.order, name='order'),
    path('api/orders/', OrderListCreateView.as_view(), name='order-create'),
    path('api/orders/<int:pk>/', OrderRetrieveAPIView.as_view(), name='order-detail'),
    path('api/users/', UserProfileListCreateView.as_view(), name='user-list-create'),
    path('api/users/<int:pk>/', UserProfileRetrieveView.as_view(), name='user-detail'),


]
