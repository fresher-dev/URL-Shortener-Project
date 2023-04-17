from django.urls import path
from . import views


app_name = "urlshortener"

urlpatterns = [
    path("", views.index, name="index"),
    path("shorten/<str:url>", views.shorten, name="shorten"),
    path("shorten", views.shorten_post, name="shorten_post"),
    path("<str:url_hash>", views.redirect_hash, name="redirect"),
]