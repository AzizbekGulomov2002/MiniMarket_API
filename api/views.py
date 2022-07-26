from django.shortcuts import render



from mahsulot.models import Mahsulot, Menyu

from .serializers import MahsulotSerializer, MenyuSerializer

from rest_framework.viewsets import ModelViewSet


class MahsulotViewSet(ModelViewSet):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer
    
class MenyuViewSet(ModelViewSet):
    queryset=Menyu.objects.all()
    serializer_class=MenyuSerializer