from django.shortcuts import render
from .serializers import MovieSerializer,MovieSerializerAPI,MainSerializer
from django.http import HttpResponse
from .models import Ratting
from collections import defaultdict
from django.apps import apps
import json
import requests

# Create your views here.
class BulkCreateManager(object):
    """
    This helper class keeps track of ORM objects to be created for multiple
    model classes, and automatically creates those objects with `bulk_create`
    when the number of objects accumulated for a given model class exceeds
    `chunk_size`.
    Upon completion of the loop that's `add()`ing objects, the developer must
    call `done()` to ensure the final set of objects is created for all models.
    """

    def __init__(self, chunk_size=100):
        self._create_queues = defaultdict(list)
        self.chunk_size = chunk_size

    def _commit(self, model_class):
        model_key = model_class._meta.label
        model_class.objects.bulk_create(self._create_queues[model_key])
        self._create_queues[model_key] = []

    def add(self, obj):
        """
        Add an object to the queue to be created, and call bulk_create if we
        have enough objs.
        """
        model_class = type(obj)
        model_key = model_class._meta.label
        self._create_queues[model_key].append(obj)
        if len(self._create_queues[model_key]) >= self.chunk_size:
            self._commit(model_class)

    def done(self):
        """
        Always call this upon completion to make sure the final partial chunk
        is saved.
        """
        for model_name, objs in self._create_queues.items():
            if len(objs) > 0:
                self._commit(apps.get_model(model_name))


def view(request):
    json_data = open("/Users/sotsys207/Desktop/Project/media/movie.json","r")
    print(json_data)   
    readfile = json_data.read()
    data1 = json.loads(readfile)
    print(data1)
    
    # bulk_mgr = BulkCreateManager(chunk_size=100)
    # for row in data1:
    #     bulk_mgr.add(Ratting(id : data["id"],
    #        adult : data["adult"],
    #        backdrop_path=row["backdrop_path"],
    #        original_language : data["original_language"], 
    #        original_title : data["original_title"], 
    #        overview : data["overview"], 
    #        popularity : data["popularity"], 
    #        poster_path : data["poster_path"], 
    #        release_date : data["release_date"], 
    #        title : data["title"], 
    #        video : data["video"], 
    #        vote_average : data["vote_average"], 
    #        vote_count : data["vote_count"]
    #     ))

    # bulk_mgr.done()


def home(request):
    queryset = Ratting.objects.all()
    return render(request,'home.html',{'queryset':queryset})

def movie_detail(request, pk):
    queryset = Ratting.objects.get(pk=pk)
    print(queryset)
    return render(request, 'movie_detail.html', {'queryset': queryset})




def requestapi(request):
    api =requests.get('https://api.themoviedb.org/3/discover/movie?api_key=c9a63529f5f0aba51994f816abbc1c95&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types=flatrate')
    data1 = api.json()
    data = json.dumps(data1)
    data2 = json.loads(data)
    print(data2['results'])
    for details in data2['results']:
        # print(details)
        # serializer = MovieSerializerAPI(data=details)
        # # print(serializer.is_valid())
        # if serializer.is_valid():
        #     serializer.save()
        result = Ratting(
            adult = details["adult"],
            backdrop_path=details["backdrop_path"],
            original_language = details["original_language"], 
            original_title = details["original_title"], 
            overview = details["overview"], 
            popularity = details["popularity"],
            poster_path = details["poster_path"],
            release_date = details["release_date"], 
            title = details["title"],
            vote_average = details["vote_average"], 
            vote_count = details["vote_count"]
        )
        result.save()


    # data = MainSerializer(data=api)

    # print(data)
    # appointment_attrs = {
    #     "adult" : data["adult"],
    #        "backdrop_path": data["backdrop_path"],
    #        "original_language" : data["original_language"], 
    #        "original_title" : data["original_title"], 
    #        "overview" : data["overview"], 
    #        "popularity" : data["popularity"], 
    #        "poster_path" : data["poster_path"], 
    #        "release_date" : data["release_date"], 
    #        "title" : data["title"], 
    #        "video" : data["video"], 
    #        "vote_average" : data["vote_average"], 
    #        "vote_count" : data["vote_count"]
    # }
    # appointment = Ratting.objects.create(**appointment_attrs)
    
    
    
    # print(api)
    # serializer = MainSerializer(data=api)
    # print(serializer.is_valid())
    # print(serializer.data['results'])
    
    # for details in data.results:
    #     serializer = MovieSerializerAPI(data=details)
    #     serializer.is_valid()
    #     print(serializer.data)
    return render(request,'home.html')









