from django.shortcuts import render

def index(request):
    
    data = {}
    
    return render(request, 'fb_test/index.html', data)