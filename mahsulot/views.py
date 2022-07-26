from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Mahsulot, Menyu

class MenyuListView(ListView):
    model = Menyu
    template_name = 'mahsulot/menyu_list.html'
    
class MahsulotListView(ListView):
    model = Mahsulot
    template_name = 'mahsulot/mahsulot_list.html'