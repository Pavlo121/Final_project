from django.shortcuts import render, redirect
from .forms import RegistrationForm
from rest_framework import generics
from .models import Order
from .models import UserProfile
from .serializers import OrderSerializer
from .serializers import UserProfileSerializer

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")  # Редирект на главную страницу
    else:
        form = RegistrationForm()
    return render(request, "my_site/register.html", {"form": form})

# МЕНЮ
def home(request):
    return render(request, "my_site/index.html")  # Просто рендер главной страницы


def g63(request):
    return render(request, "my_site/g63.html")

def e63(request):
    return render(request, "my_site/e63.html")


def gle(request):
    return render(request, "my_site/gle.html")

def S_Class(request):
    return render(request, "my_site/S_Class.html")

#ЗАКАЗИ
def order(request):
    return render(request, "my_site/order.html")

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileRetrieveView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

