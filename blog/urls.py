from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog_pro.views import CustomTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('blog_pro.urls')),
    path('api/v1/token/', CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# https://docs.djangoproject.com/en/5.1/howto/static-files/#serving-static-files-during-development
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
