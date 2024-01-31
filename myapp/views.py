from django.shortcuts import render,redirect
from .models import AnnounceText,StoreImages
from .forms import StoreImagesForm
# Create your views here.
def home(request):
    return render(request,"home.html")
def display1(request):
    obj1=AnnounceText.objects.all();
    l=len(obj1)
    obj2=obj1[l-1];
    dt=obj2.text
    imgs=StoreImages.objects.all()
    return render(request,'display.html',{'data':dt,'imgs':imgs})
def storetext(request):
    if request.method=='POST':
        txt=request.POST['text']
        AnnounceText.objects.all().delete();
        
        obj=AnnounceText.objects.create(text=txt)
        obj.save()

        #return render(request,'display.html',{'data':dt})
        return redirect(home)
    return render(request,"textform.html")
def storeImage(request):
    if request.method=='POST':
        
        name=request.POST['name']
        img=request.FILES['image']
        obj=StoreImages.objects.create(name=name,image=img)
        
        obj.save();
        return redirect(home)
    return render(request,"storeImage.html")
