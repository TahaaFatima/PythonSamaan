from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("HELLO, adoptions")

def main(request):
    return HttpResponse("HELLO, main function")