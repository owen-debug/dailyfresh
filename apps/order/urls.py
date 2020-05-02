
from django.contrib import admin
from django.urls import path
from django.urls import path,include,re_path
from order.views import OrderPlaceView
from django.conf.urls import url
app_name = 'order'
urlpatterns = [
    url(r'^place/$', OrderPlaceView.as_view(), name='place'),# 提交订单页面显示
]