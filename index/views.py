from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

class IndexView(View):
   def get(self, request, *args, **kwargs):
        return JsonResponse({'code':0})

# Create your views here.
