from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/juiceapp/login/') 
def purchase(request):
    user=request.user

    content={

        'user_id': user.id,
        'user_name': user.username
        
        }
    
    return render(request, 'purchase.html',content)