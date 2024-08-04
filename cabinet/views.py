from django.shortcuts import render
from django.http import render

def main(request):
    return render (request, 'cabinet/test_template.html')

# Create your views here.
