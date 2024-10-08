
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/auth/', include('Accounts.urls')),
    path('api/products/', include('products.urls')),
]