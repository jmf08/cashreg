from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
   path('', views.login, name='login'),
   path('Inventory/', views.inventory, name='inventory'),
   path('CashRegister/', views.Cash_Register, name='CashRegister'),
   path('CashRegister/CashRegIframe/',views.Cash_Regiframe, name='CashRegIframe'),
   path('Signup/',views.signup, name= 'Signup'),
   path('Add Inventory/',views.Add_inventory, name='AddInventory'),
   path('update/<update_id>/',views.updateitems, name='update'),
   path('delete/<update_id>/',views.deleteitems, name='delete'),
   path('delete2/<update_id2>/',views.deleteitems2, name='delete2'),
   path('delete3/<update_id3>/',views.deleteitems3, name='delete3'),
]
