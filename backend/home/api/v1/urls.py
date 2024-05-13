from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ProductViewSet, SolidViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("product", ProductViewSet)
router.register("solid", SolidViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
