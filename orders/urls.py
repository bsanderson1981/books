from django.urls import path

from .views import OrdersPageView, charge #charge for stripe add on

urlpatterns = [
    path('charge/', charge, name='charge'), # needed for stripe add on 
    path('', OrdersPageView.as_view(), name='orders'),

]
