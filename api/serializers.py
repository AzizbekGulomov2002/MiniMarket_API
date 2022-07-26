from rest_framework import serializers
from mahsulot.models import Mahsulot, Menyu

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = ('nomi', 'turi', 'mahsulot_haqida', 'rasm', 'narx')
        
class MenyuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menyu
        fields = ('nomi',)