from django.shortcuts import render
from django.views import homepage
from django.http import HttpResponse
# Create your views here.
# def homepage(request):
#     return HttpResponse("This is the home page")

def homepage(request):
    return render(request, "homeview/homepage.html")

    # return render(
    #     request,
    #     "homepage/homepage.html",
    #     {"homepage":homepage}
    # )