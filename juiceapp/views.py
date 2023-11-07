from django.shortcuts import render
from .models import *

def purchase(request):
    user=request.user
    content={
        'user_id': user.id,
        'user_name': user.username
    }
    return render(request, 'purchase.html',content)