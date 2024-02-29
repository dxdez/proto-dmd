from django.shortcuts import render
from .models import MarkdownContent

def markdown_content_view(request):
    markdown_content = MarkdownContent.objects.first()
    context = {"markdown_content": markdown_content}
    return render(
        request,
        "proto_dmd_app/markdown_content.html",
        context=context
    )
