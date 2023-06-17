from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request,'home.html')

def Aboutme(request):
    return render(request,"aboutme.html")

def Map(request):
    return render(request,"map.html")

def Story(request):
    return render(request,"story.html")

def Video(request):
    return render(request,"video.html")

def Aboutstory(request):
    return render(request,"aboutstory.html")

def Refference(request):
    return render(request,"refference.html")

def Culture(request):
    return render(request,"culture.html")

def Chinesehistory(request):
    return render(request,"chinesehistory.html")

def Chinesebuilding(request):
    return render(request,"chinesebuilding.html")

def Era1(request):
    return render(request,"era1.html")

def Era2(request):
    return render(request,"era2.html")

def Era3(request):
    return render(request,"era3.html")

def Upload(request):
    if request.method == 'POST':
        title = request.POST.get('Title')
        title = request.POST.get('Detail')
        file = request.FILES['img']
        fs = FileSystemStorage()
        fs.save('aaa.png',file)
        Name_image = str(title)+".png"
        add_content = Content(Title=title,Detail=title,Name_image=Name_image)
        add_content.save()
        return HttpResponse('Uploaded')
    return render(request, 'Upload.html')

