from django.contrib import admin
from django.urls import path
from proto_dmd_app.views import markdown_content_view, markdown_create, markdown_edit, redirect_index_view, index_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_view, name="index"),
    path("create/", markdown_create, name="markdown-create"),
    path("mc/", redirect_index_view, name="redirect-to-index"),
    path("mc/<slug:slug>/", markdown_content_view, name="markdown-content"),
    path("edit/", redirect_index_view, name="redirect-to-index"),
    path("edit/<int:id>/", markdown_edit, name="markdown-edit"),
]

