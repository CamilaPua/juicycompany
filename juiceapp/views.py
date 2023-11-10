from django.shortcuts import render, redirect, reverse, HttpResponse
from .models import *
from .forms import JuiceForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login

class Purchase(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        sale = Sale.objects.filter(client=user, is_completed=False).last()

        if sale is None:
            sale = Sale.objects.create(client=user)

        content = {
            'user_id': user.id,
            'user_name': user.username,
            'form': JuiceForm(),
            'sale': sale
        }
        return render(request, 'purchase.html', content)

    def post(self, request):
        juice_id = request.POST.get("juices")
        quantity = request.POST.get("quantity")
        user = request.user

        sale = Sale.objects.filter(client=user, is_completed=False).last()
        if sale is None:
            sale = Sale.objects.create(client=user)

        juice = Juice.objects.get(pk=juice_id)

        try:
            saleItem = SaleItem(sale=sale, juice=juice, quantity=quantity)
            saleItem.save()

        except Exception as e:
            print(f"Error creating SaleItem: {e}")

        return redirect('/juiceapp/purchase/')
    
    def complete_purchase(request):
        client=request.user
        sale = Sale.objects.filter(client=client, is_completed=False).last()
        if SaleItem.objects.filter(sale=sale).exists():
            sale.is_completed = True
            sale.save()
        
        return redirect('/juiceapp/purchase/')

    def user_login(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
        
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return render(request, 'purchase.html')
                else:
                    return HttpResponse('Your account is disabled.')
            else:
                print(f"Invalid login details:' {username}, {password}")
                return HttpResponse('Invalid login details supplied')
        else:
            return render(request, 'login.html')
