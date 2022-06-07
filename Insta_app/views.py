from django.shortcuts import render
import datetime as dt
from models import Profile,Image

# Create your views here.
def home(request):
    profile=Profile.objects.all()
    Image= Image.filter_by_profile(profile)
    return render(request,'main/home.html', {"images":images})