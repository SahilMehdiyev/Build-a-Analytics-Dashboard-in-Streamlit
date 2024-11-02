from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet



customer_router = DefaultRouter()

customer_router.register(r'customers', CustomerViewSet)

