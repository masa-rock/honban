from django.shortcuts import render
from django.shortcuts import redirect
from django.template.response import TemplateResponse

def index(request):
  return TemplateResponse(request,'toppage/index.html')
# Create your views here.
