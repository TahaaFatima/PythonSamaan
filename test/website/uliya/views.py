from django.shortcuts import render
from .models import Testimonials,Slider

# Create your views here.
def index(request):
    image_details = Testimonials.objects.all()
    slider_details = Slider.objects.all()

    context = {'image_details': image_details,
                'slider_details': slider_details
              }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def portfolio(request):
    return render(request,"contact.html")

def contact(request):
    return render(request,"portfolio.html")
