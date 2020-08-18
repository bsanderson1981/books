
from django.conf import settings # 4 user  upload media 
from django.conf.urls.static import static # 4 user  upload media
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')),

    # Local apps
    path('', include('pages.urls')),
    path('books/', include('books.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 4 user upload media