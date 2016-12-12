from django.shortcuts import render, redirect
import datetime
import random

def win_or_lose():
    number = random.randrange(0, 101)
    if number >= 50:
        return True
    else:
        return False

def index(request):
    if 'total' in request.session:
        pass
    else:
        request.session['total'] = 0
        request.session['message'] = []
    return render(request, 'Ninja_Gold_App/index.html')

def money(request):
    if request.method == 'POST':
        date = datetime.datetime.now().strftime("(%Y/%m/%d %I:%M:%S %p)")
        if request.POST['action'] == 'farm':
            num = random.randrange(10,21)
            request.session['total'] += num
            request.session['message'].append("Earned "+str(num)+" from the Farm!"+str(date))
        elif request.POST['action'] == 'cave':
            num = random.randrange(5,11)
            request.session['total'] += num
            request.session['message'].append("Earned "+str(num)+" gold from the Cave!"+str(date))
        elif request.POST['action'] == 'house':
            num = random.randrange(2,6)
            request.session['total'] += num
            request.session['message'].append("Earned "+str(num)+" gold from the House!"+str(date))
        elif request.POST['action'] == 'casino':
            if win_or_lose() == True:
                num = random.randrange(0,51)
                request.session['total'] += num
                request.session['message'].append("Earned "+str(num)+" gold from the Casino!"+str(date))
            else:
                num = random.randrange(0,51)
                request.session['total'] -= num
                request.session['message'].append("Lost "+str(num)+" gold from the Casino!"+str(date))
    return redirect('/')
