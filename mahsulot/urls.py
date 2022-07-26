from django.urls import path

from mahsulot.views import MenyuListView, MahsulotListView

urlpatterns = [
    path('', MahsulotListView.as_view(), name='home'),
    path('', MenyuListView.as_view(), name='menyu_list'),
]
