from django.shortcuts import render_to_response


# Create your views here.
def index(request):
    return render_to_response('project/index.html', {"foo": "bar"})

def blank(request):
    return render_to_response('project/blank-page.html', {"foo": "bar"})

def bootelement(request):
    return render_to_response('project/bootstrap-elements.html', {"foo": "bar"})

def bootgrid(request):
    return render_to_response('project/bootstrap-grid.html', {"foo": "bar"})

def charts(request):
    return render_to_response('project/charts.html', {"foo": "bar"})

def forms(request):
    return render_to_response('project/forms.html', {"foo": "bar"})

def indexrtl(request):
    return render_to_response('project/index-rtl.html', {"foo": "bar"})

def tables(request):
    return render_to_response('project/tables.html', {"foo": "bar"})