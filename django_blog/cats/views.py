from django.http.response import HttpResponse
from django.shortcuts import render
import requests
from functools import wraps
import time


# Create your views here.
# try out async?

# ------ for timing ------

# start_time = datetime.now()
# # my code
# end_time = datetime.now()
# print('Duration: {}'.format(end_time - start_time))

# defining my timer function,
# from https://stackoverflow.com/questions/62522117/how-can-you-calculate-execution-time-of-a-view-in-django

def timer(func):
    """helper function to estimate view execution time"""

    @wraps(func)  # used for copying func metadata
    def wrapper(*args, **kwargs):
        # record start time
        start = time.time()

        # func execution
        result = func(*args, **kwargs)

        duration = (time.time() - start) * 1000
        # output execution time to console
        print('{}() takes {:.2f} ms to execute'.format(
            func.__name__,
            duration
            ))
        return result
    return wrapper


@timer
def CatView(request):
    base_url = "https://cat-fact.herokuapp.com"
    endpoint = "/facts/random?animal_type=cat&amount=5"
    url = base_url + endpoint
    response = requests.get(url)
    context = {"title": "CATS!", "cat_facts": response.json()}
    return render(request, "cats/main.html", context)


@timer
def CatPic(request, cat_text):
    base_url = "https://cataas.com/cat"
    endpoint = f"/cute/says/{cat_text}?size=18&color=pink"
    url = base_url + endpoint
    context = {"title": "CATS!", "cat_pic": url}
    return render(request, "cats/catpic.html", context)
