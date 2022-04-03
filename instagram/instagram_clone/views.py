from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'instagram_clone/index.html')

def about(request):
    return render(request, 'instagram_clone/about.html', {'title': 'About'})