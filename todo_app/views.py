from django.shortcuts import render

# Create your views here.
def list_todo(request):
   return render(request,"index.html")