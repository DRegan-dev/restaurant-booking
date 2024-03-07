from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import Post 
# Create your views here.

# def bookings(request):
#     return HttpResponse("This is the booking page")

def bookings(request):
    return render(request, "bookings/bookings.html")


    # return render(
    #     request,
    #     "bookings/booking.html",
    #     {"bookings": bookings}
    # )