from django.shortcuts import render_to_response
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .models import Admin, Customer


def home(request):
    return render(request, 'demo/login.html')


def process(request):
    row = Admin.objects.raw("SELECT username,password FROM demo_admin where username = %s", [request.POST['username']])[0]
    if row.password == request.POST['password']:
        return render(request, 'demo/inventory.html')

    else:
        return render(request, 'demo/login.html')


def detail(request):
    #row = Customer.objects.raw("SELECT customerName , customerID FROM demo_customer")[0]
    row = Customer.objects.all().values_list('customerName', flat=True)
    return HttpResponse(list(row))


def data(request):
    cn = Customer.objects.all().values_list('customerName', flat=True)
    mob = Customer.objects.all().values_list('mobile', flat=True)
    cn = list(cn)
    mob = list(mob)
    arr = []
    for i in range(0, len(cn)):
        arr.append(cn[i] + ' ' + mob[i])
    return render_to_response('demo/auto.html', {'data': arr})


def info(request):
   # value = request.POST['customer']
    #value = value.splie()
    #value = value[0]
    #result = Customer.objects.get(customerName=value)
    return HttpResponse('value')
    #return render_to_response('demo/info.html', {'infoc': result})


def add(request):
    return render(request, 'demo/NewUser.html')


def registration(request):
    p = Customer(customerName=request.POST['fullname'], company=request.POST['Company'], mobile=request.POST['mobile'],
                 email=request.POST['email'], address=request.POST['address'])
    p.save()













