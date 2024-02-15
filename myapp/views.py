from django.shortcuts import render,redirect
from .models import AnnounceText,StoreImages,Dummy, StorePDFs,Video,TimeTable2,TimeTable3,TimeTable4
from .forms import StoreImagesForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
import requests
import pandas as pd
# Create your views here.

url = "https://sves.org.in/studentapi/api/timetable"
headers = {
  'Authorization': 'Bearer 6fsorrFRRgU49uON/HdSQWm1fzs2dlKBNz+EvfraZRjdjsy/t9vT6eTFhAS/GPTugXebNkK7TPnE4c1kMXEQf1hnBTVOz3lEgFWDdJ0xVwFjeZmq9UOV8A=='
}



# response = requests.request("GET", url, headers=headers)
# data = response.json()

# df = pd.DataFrame(data)
# print(df)


logged_in = False
def login(request):
    global logged_in
    logged_in = False
    if request.method=='POST':
        id = request.POST['username']
        provided_password = request.POST['password']
        try:
            user = User.objects.get(username=id)
        except:
            return redirect(login)
        print(user.password)
        if check_password(provided_password, user.password):
            logged_in = True
            return render(request, 'home.html',)
        else:
            return redirect(login)
    return render(request,'login.html')
def home(request):
    return redirect(login)

def directlyToHome(request):
    return render(request, 'home.html')
def aboutus(request):
    return render(request,'aboutus.html')

def storetext(request):
    global logged_in
    # print(logged_in)
    if(logged_in):
        if request.method=='POST':
            txt=request.POST['text']
            AnnounceText.objects.all().delete()
            obj=AnnounceText.objects.create(text=txt)
            obj.save()
            #return render(request,'display.html',{'data':dt})
            # return redirect(home)
            return render(request, 'home.html')
        return render(request,"textform.html")
    else:
        return redirect(login)
def storeImage(request):
    global logged_in
    # print(logged_in)
    if logged_in:
        if request.method=='POST':
            name=request.POST['name']
            img=request.FILES['image']
            txt=request.POST['txt']
            obj=StoreImages.objects.create(name=name,image=img,text=txt)
            obj.save();
            # return redirect(home)
            return render(request, 'home.html')
        return render(request,"storeImage.html")
    else:
        return redirect(login)
def domainimage(request):
    global logged_in
    # print(logged_in)
    if logged_in:
        obj1=StoreImages.objects.filter(name="Placements")
        obj2=StoreImages.objects.filter(name="Internships")
        obj3=StoreImages.objects.filter(name="sports")
        obj4=StoreImages.objects.filter(name="Achievements")
        return render(request,"display_img.html",{'data1':obj1,'data2':obj2,'data3':obj3,'data4':obj4})
    else:
        return redirect(login)
def boolchange(request):
    global logged_in
    if logged_in:
        if request.method=='POST':
            cmlst=request.POST['text']
            lst=cmlst.split(",")
            valid_ids = [id for id in lst if id.isdigit()]
            #   YourModel.objects.filter(id__in=selected_ids).update(your_attribute=1)
            StoreImages.objects.all().update(boolval=0);
            StoreImages.objects.filter(id__in=valid_ids).update(boolval=1);
            # return redirect(home)
            return render(request, 'home.html')
        return render(request,"home.html")
    else:
        return redirect(login)
#****************************************************************
def delimg(request):
    global logged_in
    # print(logged_in)
    if logged_in:
        if request.method=='POST':
            cmlst=request.POST['text']
            lst=cmlst.split(",")
            valid_ids = [id for id in lst if id.isdigit()]
            #   YourModel.objects.filter(id__in=selected_ids).update(your_attribute=1)
            #StoreImages.objects.all().update(boolval=0);
            StoreImages.objects.filter(id__in=valid_ids).delete();
            # return redirect(home)
            return render(request, 'home.html')
        obj1=StoreImages.objects.filter(name="Placements")
        obj2=StoreImages.objects.filter(name="Internships")
        obj3=StoreImages.objects.filter(name="sports")
        obj4=StoreImages.objects.filter(name="Achievements")
        return render(request,"del_img.html",{'data1':obj1,'data2':obj2,'data3':obj3,'data4':obj4})
    else:
        return redirect(login)
def delpdf(request):
    global logged_in
    # print(logged_in)
    if(logged_in):
        if request.method=='POST':
            cmlst=request.POST['text']
            lst=cmlst.split(",")
            valid_ids = [id for id in lst if id.isdigit()]
            #   YourModel.objects.filter(id__in=selected_ids).update(your_attribute=1)
            #StoreImages.objects.all().update(boolval=0);
            StorePDFs.objects.filter(id__in=valid_ids).delete();
            # return redirect(home)
            return render(request, 'home.html')
        pdf1=StorePDFs.objects.filter(name="TimeTable")
        pdf2=StorePDFs.objects.filter(name="MidExaminations")
        pdf3=StorePDFs.objects.filter(name="Semester")
        pdf4=StorePDFs.objects.filter(name="Supplementary")
        #return render(request, 'selectpdfs.html',{'pdfs':pdfs})
        return render(request, 'del_pdf.html',{'pdf1':pdf1,'pdf2':pdf2,'pdf3':pdf3,'pdf4':pdf4})
    else:
        return redirect(login)
def delvideo(request):
    global logged_in
    # print(logged_in)
    if(logged_in):
        if request.method=='POST':
            cmlst=request.POST['text']
            lst=cmlst.split(",")
            valid_ids = [id for id in lst if id.isdigit()]
            #   YourModel.objects.filter(id__in=selected_ids).update(your_attribute=1)
            #StoreImages.objects.all().update(boolval=0);
            Video.objects.filter(id__in=valid_ids).delete();
            # return redirect(home)
            return render(request, 'home.html')
        vd=Video.objects.all()
        return render(request,"del_video.html",{'videos':vd})
    else:
        return redirect(login)



def selectvideo(request):
    global logged_in
    if logged_in:
        if request.method=="POST":
            cmlst=request.POST['text']
            lst=cmlst.split(",")
            valid_ids = [id for id in lst if id.isdigit()]
            Video.objects.all().update(boolval=0);
            Video.objects.filter(id__in=valid_ids).update(boolval=1);
            # return redirect(home)
            return render(request, 'home.html')
        vd=Video.objects.all()
        return render(request,"selectvideo.html",{'videos':vd})
    else:
        return redirect(login)
    
def selectpdfs(request):
    global logged_in
    if logged_in:
        if request.method=="POST":
            cmlst=request.POST['text']
            lst=cmlst.split(",")
            valid_ids = [id for id in lst if id.isdigit()]
            StorePDFs.objects.all().update(boolval=0);
            StorePDFs.objects.filter(id__in=valid_ids).update(boolval=1);
            # return redirect(home)
            return render(request, 'home.html')
        pdfs = StorePDFs.objects.all()
        pdf1=StorePDFs.objects.filter(name="TimeTable")
        pdf2=StorePDFs.objects.filter(name="MidExaminations")
        pdf3=StorePDFs.objects.filter(name="Semester")
        pdf4=StorePDFs.objects.filter(name="Supplementary")
        #return render(request, 'selectpdfs.html',{'pdfs':pdfs})
        return render(request, 'selectpdfs.html',{'pdf1':pdf1,'pdf2':pdf2,'pdf3':pdf3,'pdf4':pdf4})
    else:
        return redirect(login)
    
def storepdfs(request):
    global logged_in
    print(logged_in)
    if logged_in:
        if request.method=='POST':
            print("took")
            pdf=request.FILES['pdf']
            name=request.POST['name']
            # print(name)
            # print(pdf)
            obj=StorePDFs.objects.create(name=name,pdf_file=pdf)
            obj.save();
            # return redirect(home)
            return render(request, 'home.html')
        return render(request,"storepdfs.html")
    else:
        return redirect(login)
def dummy(request):
    global logged_in
    print(logged_in)
    if logged_in:
        if request.method=='POST':
            val=request.POST['name']

            Dummy.objects.all().delete()
            obj=Dummy.objects.create(val=val)
            obj.save();
            if(val=='0'):
                return render(request, "home.html")
            if(val=="1"):
                return redirect(storetext)
            if(val=="2"):
                return redirect(domainimage)
            if(val=="3"):
                return redirect(selectvideo)
            if(val=='4'):
                return redirect(selectpdfs)
            # return redirect(home)
            return render(request, 'home.html')
        return render(request,"dummy.html")
    else:
        return redirect(login)
    
def storevideo(request):
    global logged_in
    print(logged_in)
    if logged_in:
        if request.method=='POST':
            vlink=request.FILES['vlink']
            obj=Video.objects.create(title="video",video_file=vlink)
            obj.save();
            # return redirect(home)
            return render(request, 'home.html')
        return render(request,"storevideo.html")
    else:
        return redirect(login)
def storeTimeTable(request):
    if request.method=='POST':
        n = int(request.POST['no_sec'])
        year = request.POST['year']
        lst=["9:30-10:30", "10:30-11:20", "11:20-12:10", "12:10-13:00", "14:00-14:50", "14:50-15:40", "15:40-16:30"]
        for i in range(n):
            sec=request.POST['sec'+str(i)]
            for j in range(7):
                mp1=request.POST['p'+str(i)+"0"+str(j)]
                mp2=request.POST['p'+str(i)+"1"+str(j)]
                mp3=request.POST['p'+str(i)+"2"+str(j)]
                mp4=request.POST['p'+str(i)+"3"+str(j)]
                mp5=request.POST['p'+str(i)+"4"+str(j)]
                mp6=request.POST['p'+str(i)+"5"+str(j)]
                #print(mp1,"  ",mp2,"  ",mp3,"  ",mp4,"  ",mp5,"  ",mp6,"  ")
                mt1=request.POST['t'+str(i)+"0"+str(j)]
                mt2=request.POST['t'+str(i)+"1"+str(j)]
                mt3=request.POST['t'+str(i)+"2"+str(j)]
                mt4=request.POST['t'+str(i)+"3"+str(j)]
                mt5=request.POST['t'+str(i)+"4"+str(j)]
                mt6=request.POST['t'+str(i)+"5"+str(j)]
                if(year=='2'):
                    obj=TimeTable2.objects.create(year_section=year+"_"+sec,mon=mp1+"_"+mt1,tue=mp2+"_"+mt2,wed=mp3+"_"+mt3,thu=mp4+"_"+mt4,fri=mp5+"_"+mt5,sat=mp6+"_"+mt6,tm=lst[j])
                elif(year=='3'):
                    obj=TimeTable3.objects.create(year_section=year+"_"+sec,mon=mp1+"_"+mt1,tue=mp2+"_"+mt2,wed=mp3+"_"+mt3,thu=mp4+"_"+mt4,fri=mp5+"_"+mt5,sat=mp6+"_"+mt6,tm=lst[j])     
                elif(year=='4'):
                    obj=TimeTable4.objects.create(year_section=year+"_"+sec,mon=mp1+"_"+mt1,tue=mp2+"_"+mt2,wed=mp3+"_"+mt3,thu=mp4+"_"+mt4,fri=mp5+"_"+mt5,sat=mp6+"_"+mt6,tm=lst[j])
        obj.save();
        return redirect(home)
    return render(request,"timetabledisp.html")
def displayTimeTable(request):
    if request.method=='POST':
        tm=request.POST['tm']
        # print(tm)
        dy=request.POST['day']
        obj1=TimeTable2.objects.filter(tm= tm)
        obj2=TimeTable3.objects.filter(tm= tm)
        obj3=TimeTable4.objects.filter(tm= tm)
        lst1=[]
        lst2=[]
        lst3=[]
        if(dy=='1'):
            for i in obj1:
                l=[]
                l.append(i.mon.split("_"))
                l.append(i.year_section.split("_"))
                lst1.append(l)
            for i in obj2:
                l=[]
                l.append(i.mon.split("_"))
                l.append(i.year_section.split("_"))
                lst2.append(l)
            for i in obj3:
                l=[]
                l.append(i.mon.split("_"))
                l.append(i.year_section.split("_"))
                lst3.append(l)
            

        elif(dy=='2'):
            for i in obj1:
                l=[]
                l.append(i.tue.split("_"))
                l.append(i.year_section.split("_"))
                lst1.append(l)
            for i in obj2:
                l=[]
                l.append(i.tue.split("_"))
                l.append(i.year_section.split("_"))
                lst2.append(l)
            for i in obj3:
                l=[]
                l.append(i.tue.split("_"))
                l.append(i.year_section.split("_"))
                lst3.append(l)
        elif(dy=='3'):
            for i in obj1:
                l=[]
                l.append(i.wed.split("_"))
                l.append(i.year_section.split("_"))
                lst1.append(l)
            for i in obj2:
                l=[]
                l.append(i.wed.split("_"))
                l.append(i.year_section.split("_"))
                lst2.append(l)
            for i in obj3:
                l=[]
                l.append(i.wed.split("_"))
                l.append(i.year_section.split("_"))
                lst3.append(l)
        elif(dy=='4'):
            for i in obj1:
                l=[]
                l.append(i.thu.split("_"))
                l.append(i.year_section.split("_"))
                lst1.append(l)
            for i in obj2:
                l=[]
                l.append(i.thu.split("_"))
                l.append(i.year_section.split("_"))
                lst2.append(l)
            for i in obj3:
                l=[]
                l.append(i.thu.split("_"))
                l.append(i.year_section.split("_"))
                lst3.append(l)
        elif(dy=='5'):
            for i in obj1:
                l=[]
                l.append(i.fri.split("_"))
                l.append(i.year_section.split("_"))
                lst1.append(l)
            for i in obj2:
                l=[]
                l.append(i.fri.split("_"))
                l.append(i.year_section.split("_"))
                lst2.append(l)
            for i in obj3:
                l=[]
                l.append(i.fri.split("_"))
                l.append(i.year_section.split("_"))
                lst3.append(l)
        elif(dy=='6'):
            for i in obj1:
                l=[]
                l.append(i.sat.split("_"))
                l.append(i.year_section.split("_"))
                lst1.append(l)
            for i in obj2:
                l=[]
                l.append(i.sat.split("_"))
                l.append(i.year_section.split("_"))
                lst2.append(l)
            for i in obj3:
                l=[]
                l.append(i.sat.split("_"))
                l.append(i.year_section.split("_"))
                lst3.append(l)
        
        return render(request,'timetabledummy.html',{'lst1':lst1,'lst2':lst2,'lst3':lst3}) 
    lst1=[]
    lst2=[]
    lst3=[]
    return render(request,'timetabledummy.html',{'lst1':lst1,'lst2':lst2,'lst3':lst3})              
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
    # print(len(pdf))
    flag = True
    lst1=[]
    lst2=[]
    lst3=[]
    val1=0
    val2=0
    val3=0
    # print((val1))
    if (dmy2==0):
        # tm=request.POST['tm']
        # print(tm)
        # dy=request.POST['day']
        # obj1=TimeTable2.objects.filter(tm= tm)
        # obj2=TimeTable3.objects.filter(tm= tm)
        # obj3=TimeTable4.objects.filter(tm= tm)
        data=''
        try:
            response = requests.request("GET", url, headers=headers)
            data = response.json()
            # print(data)
        except Exception as e:
            print(e)
        if(data=="Not working hours" or data==""):
            dt="Not working hours"
        else:
            df = pd.DataFrame(data)
            # print('hai')
            df = df[(df["branch"] == "CSE") | (df["branch"] == "CST")]
            # print(df)
            year2df = df[((df["branch"] == "CSE") | (df["branch"] == "CST")) & ((df["semester"] == "IV Semester") | (df["semester"] == "III Semester"))]
            year3df = df[((df["branch"] == "CSE") | (df["branch"] == "CST")) & ((df["semester"] == "V Semester") | (df["semester"] == "VI Semester"))]
            year4df = df[((df["branch"] == "CSE") | (df["branch"] == "CST")) & ((df["semester"] == "VII Semester") | (df["semester"] == "VIII Semester"))]
            # print(year2df)
            # print(year3df)
            # print(year4df)
            for i,r in year2df.iterrows():
                lst=[]
                lst.append(r["branch"]+"-"+r["section"])
                lst.append(r["subjectname"])
                lst.append(r["faculty"])
                lst1.append(lst)
            for i,r in year3df.iterrows():
                lst=[]
                lst.append(r["branch"]+"-"+r["section"])
                lst.append(r["subjectname"])
                lst.append(r["faculty"])
                lst2.append(lst)
            for i,r in year4df.iterrows():
                lst=[]
                lst.append(r["branch"]+"-"+r["section"])
                lst.append(r["subjectname"])
                lst.append(r["faculty"])
                lst3.append(lst)
        
        if(len(lst1)!=0):
            val1 = len(lst1)
            val2 = len(lst2)
            val3 = len(lst3)
        # print(val1, val2, val3)
    # if(val1 or val2 or val3==0  ):
    #     dmy2=1
        
    return render(request,'display.html',{'data':dt,'imgs':imgs,'val':dmy2,'videos':vd, 'flag':flag, 'pdfs':pdf,'lst1':lst1,'lst2':lst2,'lst3':lst3,"val1":val1,"val2":val2,"val3":val3})
