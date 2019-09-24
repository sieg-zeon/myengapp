from django.conf.urls import url
from django.urls import path
from . import views
from .views import HomePageView, AboutPageView, BooksPageView, booksMenuPageView

urlpatterns = [
    path('home', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('books', BooksPageView.as_view(), name='books'),
    path('booksmenu', booksMenuPageView.as_view(), name='booksmenu')

]
