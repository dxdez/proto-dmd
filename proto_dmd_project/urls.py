from django.contrib import admin
from django.urls import path
from proto_dmd_app.views import markdown_content_view
from proto_dmd_app.views import redirect_index_view
from proto_dmd_app.views import index_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_view, name="index"),
    path("mc/", redirect_index_view, name="redirect-to-index"),
    path("mc/<slug:slug>/", markdown_content_view, name="markdown-content"),
]

