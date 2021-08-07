
from django.shortcuts import render
from django.template import Template
from django.template import loader
from django.http import HttpResponse

def homeView(request):

    aw = 'Birthday Problem'

    t = {'lop':aw}

    

    temp = loader.get_template('pigoo.html')    
    return HttpResponse(temp.render(t, request))

