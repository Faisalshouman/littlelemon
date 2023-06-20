from django.shortcuts import render
from .serializers import MenuSerializer , BookingSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import MenuItem , Booking
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]    
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
