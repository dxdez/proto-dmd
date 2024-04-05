from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import MarkdownContent
from .forms import MarkdownForm

def index_view(request):
    markdown_records = MarkdownContent.objects.order_by('-id')[:10]
    context = {
        'content': {
            'title': 'Home',
            'markdown_list': markdown_records
        }
    }
    return render(
        request,
        'proto_dmd_app/index.html',
        context=context
    )

def redirect_index_view(request):
    return redirect('/')

def markdown_content_view(request, slug):
    markdown_content = get_object_or_404(MarkdownContent, slug=slug)
    context = {'markdown_content': markdown_content}
    return render(
        request,
        'proto_dmd_app/markdown_content.html',
        context=context
    )

def markdown_create(request):
    if request.method == 'POST':
        form = MarkdownForm(request.POST)
        if form.is_valid():
            form.save()    
            return HttpResponse('<p>Info Saved!</p>')
        else:
            return HttpResponse('<p>Info is not Valid</p>')
    else:
        form = MarkdownForm
        context = {
            'form': form
        }
        return render(
            request,
            'proto_dmd_app/markdown_create.html',
            context=context
        )
        
