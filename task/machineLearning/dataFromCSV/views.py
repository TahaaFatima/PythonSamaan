from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import pandas as pd


# Create your views here.
def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        
        user_data   = pd.read_csv(myfile.name)
        column_data = user_data.columns
        
        context = {
            'uploaded_file_url': uploaded_file_url,
            'user_data'        : user_data,
            'column_data'      : column_data
        }
        return render(request, 'index.html', context)

    return render(request, 'index.html')
