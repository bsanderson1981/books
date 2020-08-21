from django.contrib.auth.mixins import (
    LoginRequiredMixin, # check logged in
    PermissionRequiredMixin #new add class permissions 
)
from django.views.generic import ListView, DetailView

from .models import Book


class BookListView(LoginRequiredMixin,ListView): #LoginRequiredMixin first to check if logged in 
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login' #new 

# Create your views here.

class BookDetailView(
    LoginRequiredMixin,
    PermissionRequiredMixin,  #new add perissions 
    DetailView): #LoginRequiredMixin first to check if logged in 
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login' #new 
    permission_required = 'books.special_status' # support adding admin permissions 
