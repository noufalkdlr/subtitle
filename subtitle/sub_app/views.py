from django.shortcuts import render,redirect
from . import forms
from . models import MovieInfo

def index(request):

    if request.POST:
        frm = forms.MovieForm(request.POST,request.FILES)

        if frm.is_valid():
            frm.save()
    else:
        frm = forms.MovieForm()
    return render(request, 'index.html',{'frm':frm})
    

def list(request):
    info = MovieInfo.objects.all()

    return render(request, 'list.html',{'info': info})


def edit(request):
    return render(request, 'edit.html')

def delete(request,id):
    dele = MovieInfo.objects.get(id = id)
    dele.delete()
    return redirect('/list')