from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [

    path('', RedirectView.as_view(url='/juiceapp/')),
    path('juiceapp/', RedirectView.as_view(url='/juiceapp/purchase/')),
    path('juiceapp/purchase/', views.Purchase.as_view(), name='purchase'),
    path('juiceapp/purchase/complete_purchase/', views.Purchase.complete_purchase, name='complete_purchase')
    
]