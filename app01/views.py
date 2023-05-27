from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  return HttpResponse('主页')

def home_index(request):
  return render(request, "home_index.html")

def home_templates(request):
  return render(request, "home_templates.html")