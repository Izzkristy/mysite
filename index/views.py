from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.template.response import TemplateResponse

class IndexView(View):
   def get(self, request, *args, **kwargs):
        return TemplateResponse(request, 'index.html', {})

# Create your views here.
