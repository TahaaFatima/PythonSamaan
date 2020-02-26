from django.shortcuts import render
from .models import Testimonials,Slider,UserDetailsForm

# Create your views here.
def index(request):
    image_details = Testimonials.objects.all()
    slider_details = Slider.objects.all()

    context = {'image_details': image_details,
                'slider_details': slider_details
              }

    if request.method == "POST":
        form = UserDetailsForm()
        form.user_name         = request.POST.get('name')
        form.user_email        = request.POST.get('email')
        form.user_phone_number = request.POST.get('phone_number')
        form.user_message      = request.POST.get('message')
        form.save()

    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def portfolio(request):
    return render(request,"contact.html")

def contact(request):
    return render(request,"portfolio.html")
