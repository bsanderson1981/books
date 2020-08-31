from django.db.models import Q # needed for advance search use of  :  and or

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

class SearchResultsListView(ListView): #new
    
    model = Book

    context_object_name = 'book_list'

    template_name = 'books/search_results.html'

    #queryset = Book.objects.filter(title__icontains='beginners') #new
    def get_queryset(self): # new
       query = self.request.GET.get('q')
       return Book.objects.filter(
           Q(title__icontains=query) | Q(author__icontains=query)
       )



"""  model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
 """