from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "paulslist/dashboard.html")

def new_post(request):
    pass

def edit_post(request):
    pass
