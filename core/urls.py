from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Storefront Admin'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('home.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    # path('store/', include('store.urls')), # comment it out
    path('', include('store.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'home.views.handler404'
