from django.shortcuts import render, redirect
from .forms import RegistrationForm,LoginForm
from rest_framework import generics
from .models import Order
from .models import UserProfile
from .serializers import OrderSerializer
from .serializers import UserProfileSerializer
from django.contrib import messages
from django.contrib.auth.hashers import check_password

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")  # Редирект на главную страницу
    else:
        form = RegistrationForm()
    return render(request, "my_site/register.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Пытаемся найти пользователя по email
            try:
                user = UserProfile.objects.get(email=email)
            except UserProfile.DoesNotExist:
                messages.error(request, "Пользователь с таким Email не найден.")
                return redirect('login')

            # Проверяем хешированный пароль
            if check_password(password, user.password):
                # Сохраняем user_id в сессии, чтобы дальше считать пользователя "залогиненым"
                request.session['user_id'] = user.id
                messages.success(request, f"Добро пожаловать, {user.first_name}!")
                return redirect('index')  # Или на другую страницу после логина
            else:
                messages.error(request, "Неверный пароль.")
                return redirect('login')
    else:
        form = LoginForm()

    return render(request, 'my_site/login.html', {'form': form})

def logout_view(request):
    # Удаляем информацию о пользователе из сессии
    if 'user_id' in request.session:
        del request.session['user_id']
    messages.success(request, "Вы вышли из системы.")
    return redirect('login')

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

