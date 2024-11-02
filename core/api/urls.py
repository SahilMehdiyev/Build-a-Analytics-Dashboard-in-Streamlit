from rest_framework.routers import DefaultRouter
from django.urls import path,include
from customers.api.urls import customer_router

router = DefaultRouter()


# app 1
# app 2
# customers

router.registry.extend(customer_router.registry)

urlpatterns = [
    path('',include(router.urls)),
]

