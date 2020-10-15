from django.shortcuts import render
from django.http import HttpResponse

from .models import Quote

def index(request):
  q = Quote.objects.first()
  quote_list = Quote.objects.all()
  return render(request, 'quotes/index.html', {"quote": q, "quote_list": quote_list})


#Random
#items = model.objects.all()
#random_items = random.choice(items)