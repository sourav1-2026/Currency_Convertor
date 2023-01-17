from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here
import requests
from decouple import config


def convert(source_currency,amount,target_currency):
    url = "https://currency-converter-by-api-ninjas.p.rapidapi.com/v1/convertcurrency"

    querystring = {"have":"{}".format(source_currency),"want":"{}".format(target_currency),"amount":"{}".format(amount)}

    headers = {
            "X-RapidAPI-Key": config('X-RapidAPI-Key'),
            "X-RapidAPI-Host": config('X-RapidAPI-Host')
        }


    response = requests.request("GET", url, headers=headers, params=querystring)

    return response

        

@csrf_exempt
def ChatAppView(request):
    if request.method=='POST':
        payload = json.loads(request.body)
        source_currency=payload['queryResult']['parameters']['unit-currency']['currency']
        amount=payload['queryResult']['parameters']['unit-currency']['amount']
        target_currency=payload['queryResult']['parameters']['currency-name']
        response=convert(source_currency,amount,target_currency)
        json_data=response.json()
        result={
            'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,json_data['new_amount'],target_currency)
        }
        return JsonResponse(result)
    return HttpResponse('Response from First View') 