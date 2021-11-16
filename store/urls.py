from django.urls import path
from . import views
urlpatterns = [ 
    # path('wh1index', views.wh1index, name='wh1index'), 
    
    path('gebiOrders', views.gebiOrders, name='gebiOrders'),   
    path('wechiOrders', views.wechiOrders, name='wechiOrders'), 
    path('updateStatus/<int:oid>', views.updateStatus, name='updateStatus'),    
    # path('wh2index', views.wh2index, name='wh2index'),   
    path('confirmQuantity/<int:oid>', views.confirmQuantity, name='confirmQuantity'),  
     path('confirmorder/<int:oid>', views.confirmOrder, name='confirmorder'),    
    
]
 