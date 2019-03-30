from django.shortcuts import render

from eiam_db import models
from django.shortcuts import redirect

from django.http import HttpResponse

# Create your views here.

def index(request):
    # if len(request.session["username"]):
    #     return redirect("/UserInfo")
    if request.method =="POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # models.CmdbUserinfo.objects.create(user=username, pwd=password)
        user_list = models.CmdbUserinfo.objects.filter(user=username, pwd=password)
        if user_list.count() > 0:
            request.session["username"] = username
            request.session["model"] = user_list[0].model
            request.session.set_expiry(10)
            return redirect("/UserInfo")
        elif len(username) > 0:
            return render(request, "index.html", {"error": "error"})
    # user_list = models.CmdbUserinfo.objects.all()

    return render(request, "index.html")



def UserInfo(request):
    username = ""
    model = ""
    if request.session.get("username", None):
        username = request.session["username"]
        model = request.session["model"]
    user_list = models.DomainMessage.objects.all()
    ent_list = models.EntityMessage.objects.all()
    e = "Ea"
    d = "Da"
    did = models.DomainMessage.objects.filter(dname=d)
    did = did[0].did
    eid = models.EntityMessage.objects.filter(did=did, ename=e)
    if request.method == "POST":
        e = request.POST.get("dropdown2")
        d = request.POST.get("dropdown1")
        did = models.DomainMessage.objects.filter(dname=d)
        did = did[0].did
        eid = models.EntityMessage.objects.filter(did=did, ename=e)
    else:
        did = models.DomainMessage.objects.filter(dname=d)
        did = did[0].did
        eid = models.EntityMessage.objects.filter(did=did, ename=e)
    return render(request, "UserInfo.html", {"user": username, "data": user_list, "ent": ent_list, "eid": eid, "e": e, "d": d})

def TrustE(request):
    e_list = models.Trends.objects.all()
    esend = 2
    eres = 22
    data = models.Trends.objects.filter(resid_t=esend, reqid_t=eres)
    if request.method == "POST":
        eres = request.POST.get("dropdown2")
        esend = request.POST.get("dropdown1")
        data = models.Trends.objects.filter(resid_t=esend)

    return render(request, "TrustEvaluation.html", {"data": data, "ent": e_list, "e1": esend, "e2": eres})

def Prov(request):
    user_list = models.DomainMessage.objects.all()
    return render(request, "ProviderList.html", {"data": user_list})

def Relia(request):
    e_list = models.GValue.objects.values("eid").distinct()
    eid = 2
    list = models.GValue.objects.filter(eid=eid)
    if request.method == "POST":
        eid = request.POST.get("dropdown1")
        list = models.GValue.objects.filter(eid=eid)

    return render(request, "Reliability.html", {"e_list": e_list, "data": list, "eid": eid})

def His(request):
    year = "2018"
    month = "08"
    d = year + '-' + month
    reqid = models.EachMessage.objects.filter(date__icontains=d)

    if request.method == "POST":
        year = request.POST.get("year")
        month = request.POST.get("month")
        d = year + '-' + month
        reqid = models.EachMessage.objects.filter(date__icontains=d)

    return render(request, "HistoryTrust.html", {"reqid": reqid,  "month": month})



def sjk(request):
    user_list = models.DomainMessage.objects.all()
    ent_list = models.EntityMessage.objects.all()
    eid = 0
    year = "2018"
    month = "08"
    d = year + '-' + month
    # resid = models.EachMessage.objects.filter(date='2018-09-06')
    # reqid = models.EachMessage.objects.filter(date__month__gte=month)
    # resid = models.EachMessage.objects.only('resid').get(date__icontains=d)
    reqid = models.EachMessage.objects.filter(date__icontains=d)
    # resname = models.EntityMessage.objects.only('did').get(eid=resid)
    # reqname = models.EntityMessage.objects.only('did').get(eid=reqid)
    # resdname = models.DomainMessage.objects.filter(did=resname)
    # reqdname = models.DomainMessage.objects.filter(did=reqname)

    if request.method == "POST":
        e = request.POST.get("dropdown2")
        d = request.POST.get("dropdown1")
        did = models.DomainMessage.objects.filter(dname=d)
        eid = models.EntityMessage.objects.filter(did=did, ename=e)
        # month = request.POST.get("month")
        # reqid = models.EachMessage.objects.filter(date__month__gt=month)

    return render(request, "shujuku_test.html", {"data": user_list, "ent": ent_list, "eid": eid, "e": e, "d": d, "reqid": reqid})

def sign(request):

    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        email = request.POST.get("email")
        test = request.POST.get("test")
        model = request.POST.get("login")
        tmp = 0
        models.CmdbUserinfo.objects.create(user=username, pwd=pwd, email=email, model=model)

    return render(request, "signin.html")

def logout(requset):
    requset.session.clear()
    return redirect("/index")


