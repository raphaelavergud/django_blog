from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Blog

# Create your views here.


def home(request):
    blog_posts = Blog.objects.all()
    context = {"blog_posts": blog_posts}
    return render(request, "blog/home.html", context)
    # blog_list_html = ''
    # for blog in blog_posts:
    #     blog_list_html += f'<p><a href="/blog/{blog.id}/">{blog.title}</a></p>'
    # print(blog_posts)
    # html = f'<html><body>{blog_list_html}</body></html>'
    # return HttpResponse(html)


def blog_post(request, id=1):
    blog = Blog.objects.get(id=id)
    context = {"blog": blog}
    return render(request, "blog/blog_post.html", context)
