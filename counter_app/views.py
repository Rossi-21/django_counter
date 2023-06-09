from django.shortcuts import render

def index(request):
    counter = request.session.get('counter', 0)
    request.session['counter'] = counter + 1
    context = {
        "counter" : counter
    }
    return render(request, "index.html", context)
