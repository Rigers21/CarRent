from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from cars import views as carsViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', carsViews.home, name='home'),
    path('about/', carsViews.about, name='about'),
    path('cars/', include('cars.urls')),
    path('accounts/', include('accounts.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
