from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'disappearing_ninjas_app/index.html')
def ninjas(request):
    return render(request, 'disappearing_ninjas_app/ninjas.html')
def ninja(request, ninja_color):
    if(ninja_color == 'blue'):
        request.session['photo'] = '../static/disappearing_ninjas_app/images/leonardo.jpg'
        return render(request, 'disappearing_ninjas_app/ninja.html')
    elif(ninja_color == 'orange'):
        request.session['photo'] = '../static/disappearing_ninjas_app/images/michelangelo.jpg'
        return render(request, 'disappearing_ninjas_app/ninja.html')
    elif(ninja_color == 'red'):
        request.session['photo'] = '../static/disappearing_ninjas_app/images/raphael.jpg'
        return render(request, 'disappearing_ninjas_app/ninja.html')
    elif(ninja_color == 'purple'):
        request.session['photo'] = '../static/disappearing_ninjas_app/images/donatello.jpg'
        return render(request, 'disappearing_ninjas_app/ninja.html')
    else:
        request.session['photo'] = '../static/disappearing_ninjas_app/images/notapril.jpg'
        return render(request, 'disappearing_ninjas_app/ninja.html')
