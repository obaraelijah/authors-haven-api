from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('supersecret/', admin.site.urls),
    path("api/v1/profiles/", include("core_apps.profiles.urls")),
    path("api/v1/articles/", include("core_apps.articles.urls")),
    path("api/v1/bookmarks/", include("core_apps.bookmarks.urls")),
    path("api/v1/responses/", include("core_apps.responses.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Authors Haven API Admin"
admin.site.site_title = "Authors Haven API Admin Portal"
admin.site.index_title = "Welcome to Authors Haven API Portal"