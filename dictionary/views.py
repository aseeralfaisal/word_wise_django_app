import re
from django.shortcuts import render
from PyDictionary import PyDictionary
import requests


def index(req):
    searchText = req.GET.get("search")
    dictionary = PyDictionary()
    meaning = dictionary.meaning(searchText)["Noun"]

    API_KEY = "0aea6ae78f304618b8961111211712"
    city = "Dhaka"
    res = requests.get("http://api.weatherapi.com/v1/current.json?key=" + API_KEY + "&q=" + city)
    temp = res.json()["current"]["temp_c"]
    context = {"meaning": meaning, "temp": temp}

    return render(req, "index.html", context)
