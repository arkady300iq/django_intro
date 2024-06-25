from django.shortcuts import render
from blog.models import Blog

def blog_list(request):
    blog = Blog.objects.all()
    context = {
        "blog_list": blog,
    }
    return render(
        request,
        template_name ="blog/blog_list.html",
        context = context,
    )

def get_blog_by_id(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    context = {
        "blog": blog,
    }
    return render(
        request,
        template_name="blog/blog_details.html",
        context = context
    )

def blog_by_author(request, author_id):
    blog = Blog.objects.filter(author_id=author_id)
    context = {
        'author_id': author_id,
        'blog': blog,
    }
    return render(
        request, 
        template_name='blog/blog_author.html',
        context= context
        )