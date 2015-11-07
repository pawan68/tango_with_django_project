from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
	return HttpResponse("Hello world! <br/> <a href='/rango/about'>About</a>")