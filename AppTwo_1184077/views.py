from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return HttpResponse("<em>APLIKASI KEDUA SAYA_1184077_Alvian Daniel Sinaga</em>")

def help(request):
	helpdict = {'help_insert' : 'INI ADALAH HALAMAN HELP PAGE '}
	return render (request, 'help.html',context=helpdict)