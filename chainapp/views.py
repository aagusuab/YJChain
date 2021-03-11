from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from YJChain.blockchain import BlockChain
import json

bc = BlockChain()


# Create your views here.
def index(request):
    return HttpResponse("Hello World :D")


def blocks(request):
    if request.method == 'GET':
        bc_in_json = bc.toJSON()
        return JsonResponse(bc_in_json, safe=False)

def mine(request):
    if request.method == 'POST':
        request.


