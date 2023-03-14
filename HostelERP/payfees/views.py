from django.http import HttpResponse
from django.shortcuts import render
from .models import Dues
from datetime import datetime
# Create your views here.

def search(request):
    return render(request, 'payfees/search.html')

def show(request):
    stu_id = request.POST['student_id']
    dues = None
    #context = {}
    counter = 0
    l=[]
    if stu_id:
        dues = Dues.objects.filter(sid = stu_id).values()
        for due in dues:
            attr = {
                'Student id': due['sid'],
                'Room Fees': due['roomfees'],
                'Mess Fees': due['messfees'],
                'Total': due['totaldue'],
            }
            l = [due['sid'], due['roomfees'], due['messfees'], due['totaldue']]
            counter = 1
        context = {'attr': l}
        return render(request, 'payfees/show_individual_dues.html', context)


def update_dues(request):
    stu_id = request.POST['student_id']
    room_fees = request.POST['room_fees']
    mess_fees = request.POST['mess_fees']

    if stu_id:
        dues = Dues.objects.filter(sid = stu_id).values()
        dues1 = Dues.objects.filter(sid = stu_id).values()
        for due in dues:
            room_fees = due['roomfees'] - float(room_fees)
            mess_fees = due['messfees'] - float(mess_fees)

        dues1.update(roomfees = room_fees, messfees = mess_fees, totaldue = (room_fees + mess_fees))
        return HttpResponse("<h3>Fees paid Successfully<h3>")
