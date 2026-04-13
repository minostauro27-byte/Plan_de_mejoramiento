from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model() 


class LoginView(TokenObtainPairView):
    pass


class RegisterView(APIView):

    def post(self, request):
        data = request.data

        username = data.get('username')
        password = data.get('password')
        rol = data.get('rol')

        #  Validaciones básicas
        if not username or not password or not rol:
            return Response(
                {"error": "Faltan datos"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if rol not in ['usuario_base', 'tecnico']:
            return Response(
                {"error": "Rol inválido"},
                status=status.HTTP_400_BAD_REQUEST
            )

        #  User (modelo)
        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "El usuario ya existe"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Crear usuario
        user = User.objects.create_user(
            username=username,
            password=password,
            rol=rol
        )

        return Response(
            {"msg": "Usuario creado correctamente"},
            status=status.HTTP_201_CREATED
        )