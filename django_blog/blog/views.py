import git
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.contrib import messages

from .models import Blog
from .forms import NewUserForm

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

def item(request, item_id):
    return HttpResponse(f"Looking at {item_id}")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="blog/register.html", context={"register_form":form})


# cross site request forgery protection
@csrf_exempt
def update(request):
    # this is for the pythonanywhere webhook from github
    if request.method == "POST":
        """
        pass the path of the diectory where your project will be
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "django_blog/"
        """
        repo = git.Repo("django_blog/")
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")
