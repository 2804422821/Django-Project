from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from .models import Staff
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

def viewIndex(request):
    if request.method == "GET":
        staffList = Staff.objects.all()
        paginator = Paginator(staffList, 10)
        page = request.GET.get('page')
        try:
            staffList = paginator.page(page)
        except PageNotAnInteger:
            staffList = paginator.page(1)
        except EmptyPage:
            staffList = paginator.page(paginator.num_pages)
        return render(request, "index.html", {'staffList': staffList})

def search(request):
    if request.POST.get('select') == "员工工号":
        staffList = Staff.objects.filter(account=request.POST.get('inputValue'))
        return render(request, "index.html", {'staffList': staffList})
    elif request.POST.get('select') == "员工姓名":
        staffList = Staff.objects.filter(name=request.POST.get('inputValue'))
        return render(request, "index.html", {'staffList': staffList})
    elif request.POST.get('select') == "部门":
        staffList = Staff.objects.filter(department=request.POST.get('inputValue'))
        return render(request, "index.html", {'staffList': staffList})
    else:
        return redirect('/')

def delete(request):
    nid = request.GET.get('nid')
    Staff.objects.filter(id=nid).delete()
    return redirect('/')

def modify(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        staff = Staff.objects.filter(id=nid)
        return render(request, "modify.html", {'staff': staff})

    else:
        values = request.POST
        staff = Staff.objects.filter(id=values.get('idOutput'))
        for item in staff:
            item.name = values.get('nameOutput')
            item.account = values.get('accountOutput')
            item.birthday = values.get('birthdayOutput')
            item.gender = values.get('genderOutput')
            item.department = values.get('departmentOutput')
            item.position = values.get('positionOutput')
            item.mobile = values.get('mobileOutput')
            item.save()
    return redirect('/')

def add(request):
    if request.method == "GET":
        return render(request, "add.html")

    else:
        values = request.POST
        staff = Staff(
            name = values.get('nameInput'),
            account = values.get('accountInput'),
            birthday = values.get('birthdayInput'),
            gender = values.get('genderInput'),
            department = values.get('departmentInput'),
            position = values.get('positionInput'),
            mobile = values.get('mobileInput')
        )
        staff.save()
    return redirect('/')











