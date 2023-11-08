from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [

    path('', RedirectView.as_view(url='/juiceapp/')),
    path('juiceapp/',RedirectView.as_view(url='/juiceapp/purchase/')),
    path('juiceapp/purchase/', views.purchase, name='purchase')
    
]