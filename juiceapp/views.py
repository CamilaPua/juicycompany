from django.shortcuts import render
from .models import *

def purchase(request):
    content={
        'user_id': 0,
        'user_name': "test"
    }
    return render(request, 'purchase.html',content)