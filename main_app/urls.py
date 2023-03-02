from django.urls import path
from . import views

urlpatterns = [
    # using an empty string here make this our root route
    # view.home refers to a file to render
    # the name='home' kwarg gives the route a name
    # naming routes is optional, but best practices
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]