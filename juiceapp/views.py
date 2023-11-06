from django.shortcuts import render
from .models import Sale

def purchase(request, user_id):
    context={}
    return render(request, 'juiceapp/purchase.html',context)