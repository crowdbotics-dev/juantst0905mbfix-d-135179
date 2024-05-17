from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    FrenchViewSet,
    LiquidViewSet,
    ProductViewSet,
    SolidViewSet,
    SpanishViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("product", ProductViewSet)
router.register("solid", SolidViewSet)
router.register("liquid", LiquidViewSet)
router.register("french", FrenchViewSet)
router.register("spanish", SpanishViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
