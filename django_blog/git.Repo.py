from git import Repo

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
repo = Repo("/Users/r.vergud/Desktop/code/projects/django_blog/django_blog")
assert not repo.bare
