from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

@api_view(["GET"])
def home_view(request):
    return Response({
        "message": "Welcome!"
    })

@api_view(['GET'])
def users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# def signup(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         email = serializer.validated_data.get("email")
#         password = serializer.validated_data.get("password")
#         if User.objects.filter(email=email).exists():
#             return Response({
#                 "error": "Email is already registered."
#             })
#         serializer.save(email=email, password=password)
#         return Response({
#             "message": "User signed up successfully."
#         })
#     return Response({
#         "error": "Invalid email or password."
#     })

# @api_view(["POST"])
# def login(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         email = serializer.validated_data.get("email")
#         password = serializer.validated_data.get("password")
#         user = User.objects.filter(email=email, password=password).first()
#         if user:
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 "message": "Login successful.",
#                 "token": refresh
#             })
#         return Response({
#             "error": "Invalid email or password."
#         })
#     return Response({
#             "error": "Invalid email or password."
#         })

class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            email = request.data.get("email")
            password = request.data.get("password")
            if User.objects.filter(email=email).exists():
                return Response({
                    "error": "Email is already registered."
                })
            serializer.save(email=email, password=password)
            return Response({
                "message": "User signed up successfully."
            })
        return Response({
            "error": "Invalid email or password."
        })

class LoginView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")
            user = User.objects.filter(email=email, password=password).first()
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    "message": "Login successful.",
                    "token": str(refresh)
                })
            return Response({
                "error": "Invalid email or password."
            })
        return Response({
                "error": "Invalid email or password."
            })