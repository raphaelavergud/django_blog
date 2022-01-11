import git
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .models import Blog, Run
from .forms import NewUserForm

# Create your views here.

def home(request):
    blog_posts = Blog.objects.all()
    run_logs = Run.objects.all()
    context = {
        "blog_posts": blog_posts,
        "run_logs": run_logs
        }
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

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="blog/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("/")

def run_log(request, id=1):
    run = Run.objects.get(id=id)
    context = {"run": run}
    return render(request, "blog/run.html", context)

# cross site request forgery protection exemption to allow this
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
