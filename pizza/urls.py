from django.urls import path, include
from . import views
from rest_framework import routers
 
router = routers.DefaultRouter()
router.register('pizza', views.PizzaOrderView) 
# router.register(r'cart', views.CartView)
urlpatterns = [
    path('', include(router.urls))
]