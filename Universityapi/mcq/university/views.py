from django.shortcuts import render
from .models import *
import io
import csv

# Create your views here.
def readCsv(request):
    template = "csv_upload.html"
    data = University.objects.all()
    prompt = {
        'order': 'Order of the CSV should be University name, City',
        'profiles': data    
        }
    
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    if request.method == "POST":
        if not csv_file.name.endswith('.csv'):
            error = "This is not csv file"
            return render(request,template,{'error':error})
            
        data_set = csv_file.open('rb')
        data_set1 = data_set.read().decode('UTF-8')
        
        io_string = io.StringIO(data_set1)
        
        for column in csv.reader(io_string, delimiter=',', quotechar="|"): 
            
            _, created = University.objects.update_or_create(
                university_name = column[0],
                university_city = column[1],
                )
            
    context = {}
    return render(request,"csv_upload.html",context)
