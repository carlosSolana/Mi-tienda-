from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404,render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from miapp.models import Proveedor, Videojuego

def indice(request):
	lista_videojuegos = Videojuego.objects.all()
	return render(request, 'miapp/index.html', {'lista_videojuegos':  lista_videojuegos })


def detalle_videojuego(request,videojuego_id):
	videojuego = get_object_or_404(Videojuego, pk = videojuego_id)
	return render(request, 'miapp/detalle_videojuego.html', {'videojuego': videojuego })

def registro(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/")
	else:
		form = UserCreationForm()
	return render(request, "videojuego/registro.html", {
'form': form,})

def loginpage(request):
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate (username=username,password=password)
		if user is not None:
			login(request,user)
			return HttpResponseRedirect("/")
	else:
			form = AuthenticationForm()
	return render(request,'videojuego/login.html',{'form': form,})  

def logoutpage(request):
	logout(request)
	return HttpResponseRedirect("/")





