from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,"login.html")
def display(request):
    if request.method=='POST':
        txt=request.POST['text']
        return render(request,'display.html',{'data':txt})
    return render(request,"textform.html")
