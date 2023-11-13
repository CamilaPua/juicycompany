from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'juiceapp'

urlpatterns = [

    path('', RedirectView.as_view(url='/juiceapp/')),
    path('juiceapp/', RedirectView.as_view(url='/juiceapp/purchase/')),
    path('juiceapp/purchase/', views.Purchase.as_view(), name='purchase'),
    path('juiceapp/purchase/complete_purchase/', views.Purchase.complete_purchase, name='complete_purchase'),
    path('juiceapp/login/', views.user_login, name='user_login'),
    path('juiceapp/register/', views.register_user, name='register_login'),
    path('juiceapp/logout/', views.user_logout, name='logout'),
    path('juiceapp/bills/', views.BillsListView.as_view(), name='bills'),
    path('juiceapp/bills/bill<int:sale_id>/', views.bill_detail, name='bill_detail'),
]
