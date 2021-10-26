from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
   path('', views.login, name='login'),
   path('Inventory/', views.inventory, name='inventory'),
   path('AddInventory/',views.Add_inventory, name='AddInventory'),
   path('CashRegister/', views.Cash_Register, name='CashRegister'),
   path('CashRegIframe/',views.Cash_Regiframe, name='CashRegIframe'),
   path('Signup/',views.signup, name= 'Signup'),
]

