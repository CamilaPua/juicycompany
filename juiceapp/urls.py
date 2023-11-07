from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [

    path('purchase/', views.purchase, name='purchase'),
    path('', RedirectView.as_view(url='/juiceapp/purchase/')),

]