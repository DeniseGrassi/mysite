from django.http import HttpResponse
from django.views import generic

class PostView(generic.View):
    def get(sefl, request, *args, **lwargs):
        return HttpResponse('Hello World')
    
    