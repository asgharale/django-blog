from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/articles/', include("article.urls")),
    path('admin/', admin.site.urls),
]

# admin side custom
admin.site.site_title = "بلاگ نمونه"
admin.site.site_header = "بلاگ نمونه پنل ادمین"
admin.site.index_title = "بلاگ نمونه ادمین ساید"