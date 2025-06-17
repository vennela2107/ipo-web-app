from django.urls import path
from .views import ipo_list_view, ipo_detail_view, IPOListCreateView, IPODetailView

urlpatterns = [
    path('', ipo_list_view, name='ipo-home'),
    path('ipo/<int:id>/', ipo_detail_view, name='ipo-detail-page'),
    path('api/ipo/', IPOListCreateView.as_view(), name='ipo-list'),
    path('api/ipo/<int:pk>/', IPODetailView.as_view(), name='ipo-detail'),
]
