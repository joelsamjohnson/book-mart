from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from carton.cart import Cart
from .models import Book

from django.views.generic import ListView
from django.shortcuts import get_object_or_404


# Create your views here.


class BookList(ListView):
    model = Book
    template_name = 'list.html'


def add(request):
    cart = Cart(request.session)
    book_id = request.GET.get('book_id')
    book = get_object_or_404(Book, id=book_id)
    cart.add(book, price=book.price)
    response_data = {'success': True, 'message': 'Added to cart successfully'}
    return JsonResponse(response_data)


def remove(request):
    cart = Cart(request.session)
    book_id = request.GET.get('book_id')
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)
    response_data = {'success': True, 'message': 'Removed from cart successfully'}
    return JsonResponse(response_data)


def show(request):
    return render(request, 'cart.html')
