from django.shortcuts import render, redirect
from django.http import HttpResponse
import pyshorteners
from django.urls import reverse
from . import service


def index(request):
    return render(request, "urlshortener/index.html")


def shorten(request, url):
    shortened_url_hash = service.shorten(url)
    shortened_url = request.build_absolute_uri(reverse('urlshortener:redirect', args=[shortened_url_hash]))
    print('-==========-\n',shortened_url)
    return render(request, "urlshortener/link.html", {
        "shortened_url": shortened_url,
    })


def shorten_post(request):
    return shorten(request, request.POST['url'])


def redirect_hash(request, url_hash):
    original_url = service.load_url(url_hash).original_url
    print(original_url)
    return redirect(original_url)
