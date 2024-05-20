from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ProductViewSet,
    SolidViewSet,
    LiquidViewSet,
    FrenchViewSet,
    SpanishViewSet,
    RdscViewSet,
    RdscViewSet,
    FrenchViewSet,
    SolidViewSet,
    ProductViewSet,
    RdscViewSet,
    FrenchViewSet,
    SolidViewSet,
    ProductViewSet,
    RdscViewSet,
    FrenchViewSet,
    SolidViewSet,
    ProductViewSet,
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
router.register("rdsc", RdscViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
