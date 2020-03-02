from django.shortcuts import render

# Create your views here.
def index(request):
    """A view that display an index page"""
    return render(request, "index.html")