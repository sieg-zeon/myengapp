from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'app1/index.html'

    def get_context_data(self, **kwargs):
        params = {
            'title': 'HOME',
            'msg': 'Hello!',
            'goToHome': 'home',
        }
        return params


class AboutPageView(TemplateView):
    template_name = 'app1/about.html'

    def get_context_data(self, **kwargs):
        params = {
            'title': 'ABOUT',
            'msg': 'ABOUTのメッセージ',
            'goToHome': 'home'
        }
        return params


class BooksPageView(TemplateView):
    template_name = 'app1/books.html'

    def get_context_data(self, **kwargs):
        params = {
            'title': 'BOOKS',
            'msg': 'BOOKSのメッセージ',
            'goToHome': 'home'
        }
        return params


class booksMenuPageView(TemplateView):
    template_name = 'app1/booksmenu.html'

    def get_context_data(self, **kwargs):
        params = {
            'title': 'BOOKS MENU',
            'msg': 'BOOKS MENUのメッセージ',
            'goToHome': 'home'
        }
        return params
