from django.contrib import admin
from .models import Order
from .models import UserProfile

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Отображаем в списке
    list_display = ('id', 'first_name', 'last_name', 'phone', 'car_body_type', 'car_model', 'manager_comment', 'created_at')
    # Фильтры (слева)
    list_filter = ('car_body_type', 'created_at')
    # Поля, по которым работает строка поиска
    search_fields = ('first_name', 'last_name', 'phone', 'car_model', 'manager_comment')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email')
    list_filter = ('first_name', 'last_name')
    search_fields = ('phone', 'email', 'first_name', 'last_name')