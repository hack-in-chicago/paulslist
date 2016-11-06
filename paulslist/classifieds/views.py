from django.shortcuts import render
from classifieds.models import *

# Create your views here.
def home(request):

    countries = Post.objects.values("country").distinct()
    countries = [country.lower() for country in countries]

    latest = Post.objects.filter().order_by('-id')[:3]

    return render(request, "paulslist/dashboard.html", {'countries': countries, 'latest':latest})

def post_list(request):
    pass

def post_detail(request):
    pass
