from django.urls import path
from . import views
urlpatterns = [
    path('', views.login, name='login'),    
    path('spindex', views.spindex, name='spindex'),   
    path('shindex', views.shindex, name='shindex'),  
    path('wh1index', views.wh1index, name='wh1index'),  
    path('wh2index', views.wh2index, name='wh2index'),   
    path('stock', views.stock, name='stock'), 
]
