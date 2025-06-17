from django.shortcuts import render
from rest_framework import generics
from .models import IPO
from .serializers import IPOSerializer

def ipo_list_view(request):
    return render(request, 'ipo_app/ipo_list.html')

def ipo_detail_view(request, id):
    return render(request, 'ipo_app/ipo_detail.html')

class IPOListCreateView(generics.ListCreateAPIView):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer

class IPODetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
