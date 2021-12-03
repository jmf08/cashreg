from django.db import models
from django.forms import ModelForm
from .models import cashreg1, cashreg2, cashreg3,cashreg4,cashreg5

class cr(ModelForm):
    class Meta:
        model = cashreg1
        fields = ['ItemName', 'ProductCode','Stocks','Price']

class cr2(ModelForm):
    class Meta:
        model = cashreg2
        fields = ['ProductCode2','ItemName2','Quantity2','Price2']

class cr3(ModelForm):
    class Meta:
        model = cashreg3
        fields = ['Total3', 'Cash3','Change3']

class cr4(ModelForm):
    class Meta:
        model = cashreg4
        fields = ['ProductCode2','ItemName2','Quantity2','Price2']

class cr5(ModelForm):
    class Meta:
        model = cashreg5
        fields = ['Total3', 'Cash3','Change3']
