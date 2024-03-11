from django.shortcuts import render, get_object_or_404
from .models import MarkdownContent

def index_view(request):
    context = {"content": {"title":"Index", "content":"This the the homepage"}}
    return render(
        request,
        "proto_dmd_app/index_template.html",
        context=context
    )

def markdown_content_view(request, slug):
    markdown_content = get_object_or_404(MarkdownContent, slug=slug)
    context = {"markdown_content": markdown_content}
    return render(
        request,
        "proto_dmd_app/markdown_content.html",
        context=context
    )
