from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['title','title', 'desc', 'year']