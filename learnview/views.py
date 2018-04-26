from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
import os

# Create your views here.

def index(request):
    return render(request,'learnview/index.html')

def detail(request,id):
    context = {'number':id}
    return render(request,'learnview/detail.html',context)
#展示连接页面
def getTest1(request):
    return render(request,'learnview/getTest1.html')
#接受意见一致的情况
def getTest2(request):
    context = {'a':request.GET['a'],'b':request.GET['b'],'c':request.GET['c']}
    return render(request,'learnview/getTest2.html',context)
#接受一键多值的情况
def getTest3(request):
    context ={'a':request.GET.getlist('a'),'b':request.GET.getlist('b'),'c':request.GET['c']}
    return render(request,'learnview/getTest3.html',context)

#通过用户登录联系session
def session1(request):
    uname = request.session.get('uname','未登录')

    context = {'myname':uname}
    return render(request,'learnview/session1.html',context)

def session2(request):
    return render(request,'learnview/session2.html')

def session3(request):
    uname = request.POST['uname']
    request.session['uname'] = uname
    return redirect('/learnview/session1')
def session4(reques):
    reques.session.flush()
    return redirect('/learnview/session1')

#csrf
def csrf1(request):
    uname = request.POST['uname']
    request.session['uname'] = uname
    return redirect('/learnview/csrf1')

def uploadPic(request):
    return  render(request,'learnview/uploadPic.html')

def uploadHandle(request):
    pic1 = request.FILES["pic1"]
    picName =os.path.join(settings.MEDIA_ROOT,pic1.name)
    with open(picName,'wb+') as pic:
        for c in pic1.chunks():
            pic.write(c)
    pic.close()
    return HttpResponse('<img src="/static/media/learnview/%s"/>' %pic1.name)
