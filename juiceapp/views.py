from django.shortcuts import render
from .models import *
from .forms import JuiceForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required() 
def purchase(request):
    user=request.user

    content={

        'user_id': user.id,
        'user_name': user.username,
        'form': JuiceForm()
        
        }
    
    return render(request, 'purchase.html',content)