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


