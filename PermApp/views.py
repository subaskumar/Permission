# from django.shortcuts import render,redirect
# from .forms import SignUpForm,UserLoginForm
# from django.contrib.auth import login,authenticate,logout
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
# from django.core import serializers

from .models import Blog
from rest_framework.response import Response
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.generics import CreateAPIView
########### Build API by using Regular Django #################

# def Blog_list(request):
#     blogs = Blog.objects.all()
#     data = serializers.serialize("json", blogs,fields=('title','body'))
#     return HttpResponse(data)

from rest_framework.viewsets import  ViewSet,ModelViewSet
class Blog_list(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # authentication_classes = [SessionAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    
class RegisterView(CreateAPIView):
    # queryset = User.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = RegisterSerializer