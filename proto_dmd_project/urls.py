from django.contrib import admin
from django.urls import path
from proto_dmd_app.views import markdown_content_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "markdown-content/", markdown_content_view, name="markdown-content"
    ),
]

