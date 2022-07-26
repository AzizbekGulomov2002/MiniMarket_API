from django.urls import path, include
from .views import  MahsulotViewSet, MenyuViewSet


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Menyu', MenyuViewSet)
router.register('Mahsulot',MahsulotViewSet)

urlpatterns = [
    path("", include(router.urls))
]
