from django.shortcuts import render, redirect,HttpResponseRedirect,HttpResponse
from .models import Image
from .forms import ImageForm,ImageLike,UserForm
from django.db.models import F
from django.contrib.auth import authenticate ,login,logout
import os
from django.dispatch import receiver  #for deleting hardrive copy
from django.db import models
import shutil
# Create your views here.
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
def index(request):
    if request.method == 'GET' :
        if not request.user.is_authenticated():
            return redirect('/login')

        else:
            albums = Image.objects.filter(user=request.user)
            #albums = Image.objects.all()
            context = {
            'albums': albums,
            'user':request.user
                }
            return render(request,'openpickr/index.html',context)

    elif request.method == 'POST':
        form = ImageLike(request.POST)
        print("name"+request.POST['name'])
        #print("like" + request.POST['is_like'])
        if form.is_valid():
            #Students.objects.select_for_update().filter(id=3).update(score=10)
            Image.objects.select_for_update().filter(name=request.POST['name']).update(likes=F('likes')+1)
            Image.objects.select_for_update().filter(name=request.POST['name']).update(is_like=True)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("not valid")



def addimage(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            # image = form.save(commit=False)
            print("form is valid")
            album = form.save(commit=False)
            album.user = request.user
            album.save()
            return HttpResponseRedirect('/')
        else:
            context = {
                "form": form,
            }
            return render(request, 'openpickr/addimage.html', context)
    else:
        form = ImageForm()
        return render(request, 'openpickr/addimage.html', {'form':form})


def logmein(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                print("user active")
                login(request, user)
                albums = Image.objects.filter(user=request.user)
                return HttpResponseRedirect('/')
            else:
                print("user not active")
                return render(request, 'openpickr/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'openpickr/login.html', {'error_message': 'Invalid login'})
    return render(request, 'openpickr/login.html')


def logmeout(request):
    logout(request)
    return redirect('/login')



def signup(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Image.objects.filter(user=request.user)
                return render(request, 'openpickr/index.html', {'albums': albums})
    context = {
        "form": form,
    }
    return render(request, 'openpickr/registration.html', context)



@receiver(models.signals.post_delete, sender=Image)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    print(instance.image.path)
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
            shutil.rmtree("/home/sid/PycharmProjects/openpics/media/CACHE/images/images/"+instance.image.path[48:-4])


def deleteimg(request,image_id):
    image = Image.objects.filter(pk=image_id)
    image.delete()
    return HttpResponseRedirect('/')
