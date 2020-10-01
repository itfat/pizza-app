from django.urls import path, include
from . import views
from rest_framework import routers
 
router = routers.SimpleRouter()
router.register('cart', views.CartView) 
urlpatterns = [
    path('', include(router.urls))
]