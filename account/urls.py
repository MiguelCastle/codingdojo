from django.urls import path, include
from .views import UserViewSet, BorrowerViewSet
from rest_framework.routers import DefaultRouter
import account.views

router = DefaultRouter()
router.register('users/', UserViewSet)
# router.register('users/(?P<id>\d+)/?', UserViewSet)
router.register('users/(?P<id>[a-z0-9]+)/?', UserViewSet)

router.register(r'borrower', BorrowerViewSet, basename="Borrower")

urlpatterns = [
    path('api/', include(router.urls)),
]