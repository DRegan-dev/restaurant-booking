from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return HttpResponse("This is the home page")

    return render(
        request,
        "homepage/homepage.html",
        {"homepage":homepage}
    )