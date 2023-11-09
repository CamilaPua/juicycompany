from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import JuiceForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

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