from django.shortcuts import render,redirect
from .serializers import MovieSerializer
from django.http import HttpResponse
from .models import Ratting
import json




def view(request):
    json_data = open('/Users/sotsys207/Downloads/DjangoProjects/webtraining/Loginapis/media/movie.json',"r")
    print(json_data)   
    readfile = json_data.read()
    data1 = json.loads(readfile)
    print(data1)
        # parsed_json = json.load(data)

    for i in data1:
        data = MovieSerializer(data=i)
        print(data)
        if data.is_valid():
            print('ho')
            data.save()
    return HttpResponse('Data Entered from File')
    # for result in  data1:
        
    #     Ratting.objects.create(
    #        id = result["id"],
    #        adult = result["adult"],
    #        backdrop_path=result["backdrop_path"],
    #        original_language = result["original_language"], 
    #        original_title = result["original_title"], 
    #        overview = result["overview"], 
    #        popularity = result["popularity"], 
    #        poster_path = result["poster_path"], 
    #        release_date = result["release_date"], 
    #        title = result["title"], 
    #        video = result["video"], 
    #        vote_average = result["vote_average"], 
    #        vote_count = result['vote_count"], 
    #      ) 

