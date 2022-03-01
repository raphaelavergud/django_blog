from django.http.response import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.


def CatView(request):
    base_url = "https://cat-fact.herokuapp.com"
    endpoint = "/facts/random?animal_type=cat&amount=5"
    url = base_url + endpoint
    response = requests.get(url)
    context = {"title": "CATS!", "cat_facts": response.json()}
    print(response.json())
    return render(request, "cats/main.html", context)

def CatPic(request, cat_text):
    base_url = "https://cataas.com/cat"
    endpoint = f"/cute/says/{cat_text}?size=18&color=pink"
    url = base_url + endpoint
    context = {"title": "CATS!", "cat_pic": url}
    return render(request, "cats/catpic.html", context)
