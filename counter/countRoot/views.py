from django.shortcuts import render, redirect

# Create your views here.
#Have the root route render a template that displays the number of times the client has visited this site. 
def index(request):
    if ('num' not in request.session):
        request.session['num'] = 0
    else:
       request.session['num'] += 1 

    return render(request, "index.html")

#Add a "/destroy_session" route that clears the session and redirects to the root route. 
#BONUS: Add a Reset button that uses the "/destroy_session" route
def destroy_session(request):
    del request.session['num']

    return redirect('/')

#BONUS: Add a +2 button underneath the counter and a new route that will increment the counter by 2
def add_2(request):
    request.session['num'] += 1

    return redirect('/')

#BONUS: Add a form that allows the user to specify the increment of the counter and have the counter increment accordingly
def selection(request):
    sel = request.POST['selection']
    request.session['num'] += int(sel) - 1
    return redirect('/')

