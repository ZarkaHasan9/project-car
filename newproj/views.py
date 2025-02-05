from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import userForm
from service.models import Service
def homePage(request):
    # servicesData=Service.objects.all()
    # for a in servicesData:
    #     print(a.service_icon)
    # print(service)
    return render(request,"index.html") 
def rent(request):
    return render(request,"rent.html")
def about(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"aboutus.html",{'output':output})
def service(request):
    servicesData=Service.objects.all().order_by('service_title')[0:3]
    # for a in servicesData:
    #     print(a.service_icon)
    # print(service)
    data={
        'servicesData':servicesData
    }
    return render(request,"services.html",data) 
def ride(request):
    return render(request,"ride.html")
def courseDetails(request,courseid):
    return HttpResponse(courseid)
def signup(request):
    return render(request,"signup.html")
# def signin(request):
#     return render(request,"signin.html")

def submitForm(request):
    try:
        if request.method=='POST':
        #n=int(request.GET['num1'])
        #n2=int(request.GET['num2'])
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalans=n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'output':finalans
            }
            return HttpResponse(finalans)
    except:
        pass
def userForm(request):
    finalans = 0
    fnn = None  # Replace with an actual form instance, e.g., SomeForm()

    data = {'form': fnn}

    try:
        if request.method == 'POST':
            n1 = int(request.POST.get('num1', 0))
            n2 = int(request.POST.get('num2', 0))
            finalans = n1 + n2

            data = {
                'n1': n1,
                'n2': n2,
                'form': fnn,
                'output': finalans
            }

            url = "/about/?output={}".format(finalans)
            return redirect(url)
    except Exception as e:
        print(f"Error: {e}")
    
    return render(request, "userform.html", data)