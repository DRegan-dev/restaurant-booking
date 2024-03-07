from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import Post 
# Create your views here.

# def bookings(request):
#     return HttpResponse("This is the booking page")

class BookingPage(generic.CreateView):
    template_name = "bookings/booking.html"

    return render(
        request,
        "bookings/booking.html",
        {"bookings": bookings}
    )