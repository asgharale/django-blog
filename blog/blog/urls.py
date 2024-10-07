from django.contrib import admin
from django.conf.urls.static import static  
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('api/articles/', include("article.urls")),
    path('api/sort/', include("sort.urls")),
    path('api/user/', include("user.urls")),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

# admin side custom
admin.site.site_title = "بلاگ نمونه"
admin.site.site_header = "بلاگ نمونه پنل ادمین"
admin.site.index_title = "بلاگ نمونه ادمین ساید"
