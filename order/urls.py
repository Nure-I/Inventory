from django.urls import path
from . import views
urlpatterns = [ 
    # path('wh1index', views.wh1index, name='wh1index'), 
    path('orderhistory', views.orderHistory, name='orderhistory'),
    path('makeorder', views.makeOrder, name='makeorder'),   
    path('editorder/<int:oid>', views.editOrder, name='editorder'),
    path('outorder', views.outOrder, name='outorder'),   
    path('inorder', views.inOrder, name='inorder'),   
    path('productlist', views.productList, name='productlist'),   
    path('cancel', views.cancel, name='cancel'),   
     
    
]
 