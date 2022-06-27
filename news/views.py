from unicodedata import category
from django.shortcuts import render
import requests

api_key='=c1fdf9e7209444ca903f8ecfbf367632'
# Create your views here.
def home(request):
    country=request.GET.get('country')
    category=request.GET.get('category')
    if country:
     url=f"https://newsapi.org/v2/top-headlines?country={country}&apiKey{api_key}"
     response=requests.get(url)
     data=response.json()
     articles=data['articles']
    else:
     url=f"https://newsapi.org/v2/top-headlines?category={category}&apiKey{api_key}"
     response=requests.get(url)
     data=response.json()
     articles=data['articles']


    
    
    context={
        'articles':articles
    }

    return render(request,'news/index.html',context)