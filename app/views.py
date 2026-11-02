from django.shortcuts import render
from django.http import HttpResponse,response


# Create your views here.

def detail(request,voter_id):
    return HttpResponse("Ur looking at voter id %s" % voter_id)

def result(request,voter_id):
    return HttpResponse(response , voter_id )

def vote(request,voter_id):
    return HttpResponse("ur voting on party is %s" % voter_id)

