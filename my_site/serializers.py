from rest_framework import serializers
from .models import Order
from .models import UserProfile

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        # или перечислите нужные поля, если не хотите использовать все:
        # fields = ('id', 'first_name', 'last_name', 'phone', 'car_body_type', 'car_model', 'created_at')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'





