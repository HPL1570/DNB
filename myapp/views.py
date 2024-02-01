from django.shortcuts import render,redirect
from .models import AnnounceText,StoreImages,Dummy, StorePDFs,Video
from .forms import StoreImagesForm
# Create your views here.
def home(request):
    return render(request,"home.html")
def display1(request):
    obj1=AnnounceText.objects.all();
    dmy=Dummy.objects.all()
    dmy1=dmy[0]
    dmy2=dmy1.val
    l=len(obj1)
    obj2=obj1[l-1];
    dt=obj2.text
    imgs=StoreImages.objects.filter(boolval=1)
    vd=Video.objects.filter(boolval=1)
    pdf = StorePDFs.objects.filter(boolval=1)
    print(len(pdf))
    flag = True
    return render(request,'dis123.html',{'data':dt,'imgs':imgs,'val':dmy2,'videos':vd, 'flag':flag, 'pdfs':pdf})
def storetext(request):
    if request.method=='POST':
        txt=request.POST['text']
        AnnounceText.objects.all().delete()
        
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
def domainimage(request):
    obj1=StoreImages.objects.filter(name="Placements")
    obj2=StoreImages.objects.filter(name="Internships")
    obj3=StoreImages.objects.filter(name="sports")
    obj4=StoreImages.objects.filter(name="Achievements")
    return render(request,"display_img.html",{'data1':obj1,'data2':obj2,'data3':obj3,'data4':obj4})
def boolchange(request):
    if request.method=='POST':
        cmlst=request.POST['text']
        lst=cmlst.split(",")
        valid_ids = [id for id in lst if id.isdigit()]
        #YourModel.objects.filter(id__in=selected_ids).update(your_attribute=1)
        StoreImages.objects.all().update(boolval=0);
        StoreImages.objects.filter(id__in=valid_ids).update(boolval=1);

        return redirect(home)
    return render(request,"home.html")
def selectvideo(request):
    if request.method=="POST":
        cmlst=request.POST['text']
        lst=cmlst.split(",")
        valid_ids = [id for id in lst if id.isdigit()]
        Video.objects.all().update(boolval=0);
        Video.objects.filter(id__in=valid_ids).update(boolval=1);
        return redirect(home)
    
    vd=Video.objects.all()
    return render(request,"selectvideo.html",{'videos':vd})

def selectpdfs(request):
    if request.method=="POST":
        cmlst=request.POST['text']
        lst=cmlst.split(",")
        valid_ids = [id for id in lst if id.isdigit()]
        StorePDFs.objects.all().update(boolval=0);
        StorePDFs.objects.filter(id__in=valid_ids).update(boolval=1);
        return redirect(home)
    pdfs = StorePDFs.objects.all()
    return render(request, 'selectpdfs.html',{'pdfs':pdfs})
def storepdfs(request):
    if request.method=='POST':
        pdf=request.FILES['pdf']
        obj=StorePDFs.objects.create(pdf_file=pdf)
        obj.save();
        return redirect(home)
    return render(request,"storepdfs.html")


def dummy(request):
    if request.method=='POST':
        val=request.POST['name']

        Dummy.objects.all().delete()
        obj=Dummy.objects.create(val=val)
        obj.save();
        if(val=="1"):
            return redirect(storetext)
        if(val=="2"):
            return redirect(domainimage)
        if(val=="3"):
            return redirect(selectvideo)
        if(val=='4'):
            return redirect(selectpdfs)
        return redirect(home)
    return render(request,"dummy.html")
def storevideo(request):
    if request.method=='POST':
        vlink=request.FILES['vlink']
        obj=Video.objects.create(title="video",video_file=vlink)
        obj.save();
        return redirect(home)
    return render(request,"storevideo.html")
