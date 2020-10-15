from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return render(request, 'quotes/index.html', {})


#Random
#items = model.objects.all()
#random_items = random.choice(items)