from django.urls import path, include
from .views import UserViewSet, BorrowerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet)
router.register(r'borrower', BorrowerViewSet, basename="Borrower")
urlpatterns = [
    path('api/', include(router.urls)),
]