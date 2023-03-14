from django.shortcuts import render
from .models import Studentinfo

# Create your views here.
def studentinfo(request):
    return render(request, 'studentinfo/studentinfo.html', {'context':Studentinfo.objects.all()})

def form(request):
    return render(request, 'registration/form1.html')

def update(request):
    first_name = request.POST['name1']
    last_name = request.POST['name2']
    sex = request.POST['sex']
    adhaar = request.POST['adhaar']
    mobile = request.POST['mobile']
    pname = request.POST['pname']
    pmobile = request.POST['pmobile']
    ad1 = request.POST['ad1']
    ad2 = request.POST['ad2']
    city = request.POST['city']
    pin = request.POST['pin']
    gname = request.POST['gname']
    gmobile = request.POST['gmobile']
    iname = request.POST['iname']
    hname = request.POST['hname']
    hmobile = request.POST['hmobile']
            #print(first_name, last_name)

    student_info_object = Studentinfo()
    student_info_object.first_name = first_name
    student_info_object.last_name = last_name
    student_info_object.sex = sex
    student_info_object.adhaar = adhaar
    student_info_object.mobile_no = mobile
    student_info_object.parent_name = pname
    student_info_object.parent_mobile = pmobile
    student_info_object.address_l1 = ad1
    student_info_object.address_l2 = ad2
    student_info_object.city = city
    student_info_object.pin_code = pin
    student_info_object.guardian_name = gname
    student_info_object.guardian_mobile = gmobile
    student_info_object.institution_name = iname
    student_info_object.hod_name = hname
    student_info_object.hod_mobile = hmobile

    student_info_object.save()

    attr = {
        'Student id': student_info_object.sid,
        'First name':student_info_object.first_name,
        'Last name':student_info_object.last_name,
        'Sex':student_info_object.sex,
        'Adhaar Card no.':student_info_object.adhaar,
        'Mobile':student_info_object.mobile_no,
        'Parent Name':student_info_object.parent_name,
        'Parent Mobile':student_info_object.parent_mobile,
        'Address line 1':student_info_object.address_l1,
        'Address line 2':student_info_object.address_l2,
        'City':student_info_object.city,
        'Pin Code':student_info_object.pin_code,
        'Guardian Name':student_info_object.guardian_name,
        'Guardian Mobile':student_info_object.guardian_mobile,
        'Registration Date':student_info_object.registration_date,
        'Institution Name':student_info_object.institution_name,
        'HOD Name':student_info_object.hod_name,
        'HOD Mobile':student_info_object.hod_mobile
    }
    context = {'attr':attr}

    return render(request, 'registration/form.html', context)