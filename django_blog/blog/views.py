import git
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import logging

from .models import Blog, CustomAccountManager, Run
from .forms import NewUserForm, NewPostForm, NewRunForm

# module level logger:
logger = logging.getLogger(__name__)

# Create your views here.

def home(request):
    blog_posts = Blog.objects.all()
    run_logs = Run.objects.all()
    context = {
        "blog_posts": blog_posts,
        "run_logs": run_logs,
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

def add_post(request):
    if request.method == "POST":
        form = NewPostForm(request.POST, logged_in_user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Added new blog post successfully.")
            return redirect("/")
        messages.error(request, "Unsuccessful. Could not add new blog post.")
    form = NewPostForm()
    return render(
        request=request,
        template_name="blog/add_post.html",
        context={"addpost_form": form},
    )


def item(request, item_id):
    if item_id == "hacker":
        logger.warning("a hacker is trying to hack")
    return HttpResponse(f"Looking at {item_id}")


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(
        request=request,
        template_name="blog/register.html",
        context={"register_form": form},
    )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password."), logger.info(
                    "someone is entering invalid credentials"
                )
        else:
            messages.error(request, "Invalid username or password."), logger.info(
                "someone is entering invalid credentials"
            )
    form = AuthenticationForm()
    return render(
        request=request, template_name="blog/login.html", context={"login_form": form}
    )


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")


def run_log(request, id=1):
    run = Run.objects.get(id=id)
    context = {"run": run}
    return render(request, "blog/run.html", context)

def add_run(request):
    if request.method == "POST":
        form = NewRunForm(request.POST, logged_in_user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Logged run successfully.")
            return redirect("/")
        messages.error(request, "Unsuccessful. Could not log run.")
    form = NewRunForm()
    return render(
        request=request,
        template_name="blog/add_run.html",
        context={"addrun_form": form},
    )


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
