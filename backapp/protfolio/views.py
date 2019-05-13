from django.shortcuts import render, HttpResponse
from .models import FontModel



def IndexViews(request):


     template = 'index.html'
     view = FontModel.objects.all()
     contaxt = {
          'views' : view
     }
     return render(request, template, contaxt)