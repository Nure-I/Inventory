from django.urls import path
from . import views
urlpatterns = [
    path('fReport', views.fReport, name='fReport'),    
    path('orderReport', views.orderReport, name='orderReport'),   
    path('inOrderDetail', views.inOrderDetail, name='inOrderDetail'),  
    path('outOrderDetail', views.outOrderDetail, name='outOrderDetail'), 
     path('detailO/<int:oid>', views.detailO, name='detailO'),  
]