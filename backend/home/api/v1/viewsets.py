from rest_framework import viewsets
from home.models import (
    Product,
    Solid,
    Liquid,
    French,
    Spanish,
    Rdsc,
    Rdsc,
    French,
    Solid,
    Product,
    Rdsc,
    French,
    Solid,
    Product,
)
from .serializers import (
    ProductSerializer,
    SolidSerializer,
    LiquidSerializer,
    FrenchSerializer,
    SpanishSerializer,
    RdscSerializer,
    RdscSerializer,
    FrenchSerializer,
    SolidSerializer,
    ProductSerializer,
    RdscSerializer,
    FrenchSerializer,
    SolidSerializer,
    ProductSerializer,
)
from rest_framework import authentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from home.api.v1.serializers import (
    SignupSerializer,
    UserSerializer,
)


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Product.objects.all()


class SolidViewSet(viewsets.ModelViewSet):
    serializer_class = SolidSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Solid.objects.all()


class LiquidViewSet(viewsets.ModelViewSet):
    serializer_class = LiquidSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Liquid.objects.all()


class FrenchViewSet(viewsets.ModelViewSet):
    serializer_class = FrenchSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = French.objects.all()


class SpanishViewSet(viewsets.ModelViewSet):
    serializer_class = SpanishSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Spanish.objects.all()


class RdscViewSet(viewsets.ModelViewSet):
    serializer_class = RdscSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Rdsc.objects.all()
