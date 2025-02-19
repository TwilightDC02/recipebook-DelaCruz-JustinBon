from django.shortcuts import render, HttpResponse
from django.template import loader

def recipe_list(request):
    template = loader.get_template('recipelist.html')
    return HttpResponse(template.render())    

# Create your views here.
