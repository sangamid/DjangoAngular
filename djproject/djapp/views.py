from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import *
from .models import *

class CustomersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer