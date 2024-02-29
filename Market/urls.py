from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), # home is not used so that home page gets open by default
    path("Explore/", views.explore, name="explore"),
    # path("Item Details/", views.details, name="details"),
    path("About/", views.about, name="author"),
    path("Contact/", views.contact, name="create"),
]