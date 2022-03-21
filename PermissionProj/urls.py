
from django.contrib import admin
from django.urls import path,include
from PermApp import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import ( TokenObtainPairView,TokenRefreshView,TokenVerifyView)
# Creating router object
router = DefaultRouter()

# register the router object
router.register('blog_api', views.Blog_list, basename='blog')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('blogs/', views.Blog_list),
    path("auth/", include('rest_framework.urls', namespace='rest_framework')), # it use of session authentication
    path('api/', include(router.urls)),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('api/gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]