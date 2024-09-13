from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginViewSet, RegisterViewSet, APIRootView

# Create the router
router = DefaultRouter()

# Register the custom ViewSets
router.register(r'login', LoginViewSet, basename='login')
router.register(r'register', RegisterViewSet, basename='register')

# Include router URLs and add the custom API root
urlpatterns = [
    path('', APIRootView.as_view(), name='api-root'),  # Custom API root view
    path('', include(router.urls)),
]
