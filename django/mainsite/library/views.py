from django.shortcuts import render, reverse
from .models import Book, Author, RentalStatus
from django.utils import timezone

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

def index(request):

    books = Book.objects.all()
    # out_books = RentalStatus.objects.filter(checked_in=False)
    return render(request, 'library/index.html', {'books':books})


def checkout(request):
    print(request.POST)

    book_id = request.POST['book_id']
    user_name = request.POST['user_name']

    rental_status = RentalStatus(book_id=book_id, checked_in=False, user=user_name, timestamp=timezone.now())
    rental_status.save()
    #title = Book.objects.get(pk=book_id)
    #print(title)
    # RentalStatus.checked_in['book_id'] = False
    # rental_status = request.POST

    # # get the book with this id
    # # set it to 'checked out'
    # # redirect back to the index page

    #return render(request, 'library/checkout.html', {'title':title})
    return HttpResponseRedirect(reverse('library:index'))

def checkin(request):
    print(request.POST)

    book_id = request.POST['book_id']
    user_name = request.POST['user_name']

    rental_status = RentalStatus(book_id=book_id, checked_in=True, user=user_name, timestamp=timezone.now())
    rental_status.save()
    return HttpResponseRedirect(reverse('library:index'))

def rentallog(request):
    rental_statuses = RentalStatus.objects.all()
    #print(rental_statuses)

    return render(request, 'library/rentallog.html', {'rental_statuses':rental_statuses})
    # return HttpResponse('ok')