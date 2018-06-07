'''
Created on 2018. 6. 5.

@author: ime203
'''
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
