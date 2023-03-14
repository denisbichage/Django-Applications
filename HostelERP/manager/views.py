from django.shortcuts import render
from .models import EmployeeInfo
from django.http import HttpResponse
from .models import EmployeeInfo


# Create your views here.
def register(request):
    return render(request, 'registration1/register.html')


def logout(request):
   try:
      del request.session['userid']
   except:
      pass
   return render(request, 'login.html')


def login(request):
    if request.session.has_key('userid'):
        userid = request.session['userid']
        return render(request, 'loggedin.html', {"userid": userid})
    else:
        return render(request, 'login.html', {})


def startsession(request):
    userid = request.POST['userid']
    userpass = request.POST['userpass']
    object = EmployeeInfo.objects.get(empid = userid, password = userpass)
    if object.first_name != "" and object.employee_type == "manager":
        request.session['userid'] = userid
        attr = {'userid': userid}
        context = {'attr': attr}
        return render(request, 'loggedin.html', context)
    else: return render(request, 'login.html', {})


def update(request):
    first_name = request.POST['name1']
    last_name = request.POST['name2']
    sex = request.POST['sex']
    aadhaar = request.POST['aadhaar']
    mobile = request.POST['mobile']
    pname = request.POST['pname']
    pmobile = request.POST['pmobile']
    ad1 = request.POST['ad1']
    ad2 = request.POST['ad2']
    city = request.POST['city']
    pin = request.POST['pin']
    pass1 = request.POST['pass1']

    Manager_info_object = EmployeeInfo()
    Manager_info_object.first_name = first_name
    Manager_info_object.last_name = last_name
    Manager_info_object.sex = sex
    Manager_info_object.adhaar = aadhaar
    Manager_info_object.mobile_no = mobile
    Manager_info_object.parent_name = pname
    Manager_info_object.parent_mobile = pmobile
    Manager_info_object.address_l1 = ad1
    Manager_info_object.address_l2 = ad2
    Manager_info_object.city = city
    Manager_info_object.pin_code = pin
    Manager_info_object.password = pass1

    Manager_info_object.save()

    return HttpResponse("<H1>Registered successfully</H1>")