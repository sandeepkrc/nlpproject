from django.shortcuts import render
from .forms import Contactus,Intern,Consultform,Payments
from .models import Contact,InternShip,Consult


def home(request):
    return render(request,'home2.html')
def about(request):
    return render(request,'about.html')
def products(request):
    return render(request,'product.html')
def consulting(request):
    form=Consultform()
    context={'form':form}
    return render(request,'consulting.html',context)
    # ADD A FORM
    #save in db
def cnsal_save(request):
    if request.method =='POST':
        fn = request.POST['first_name']
        number = request.POST['phone_no']
        eml = request.POST['email']
        dtl = request.POST['detaits_of_consultions']
        desc = request.POST['appointment']
        c=Consult(name =fn,number=number,email_address= eml,detail=dtl,appoint=desc)
        c.save()
    return render(request,'cnsl_save.html')
    

def service(request):
    return render(request,'service.html')
def training(request):
    return render(request,'training.html')
def career(request):
    return render(request,'career.html')
def internship(request):
    return render(request,'internship.html')
def contact(request):
    form=Contactus()
    context = {'form':form}
    return render(request,'contact.html',context)
def intern_apply(request):
    iform=Intern()
    context = {'iform':iform}
    return render(request,"frmin.html",context)
def thank(request):#contact
    if request.method =='POST':
        em = request.POST['email_address']
        nm = request.POST['name']
        nbr = request.POST['number']
        msg = request.POST['message']
        c=Contact(email=em,name=nm,number=nbr,message=msg)
        c.save()
    return render(request,'thank.html')
def ithank(request):#internship
    if request.method=="POST":
        n=request.POST['name']
        e=request.POST['email_address']
        m=request.POST['number']
        c=request.POST['cover_letter']
        r=request.POST['upload_resume']
        isave = InternShip(name = n,email_address=e,number=m,cover=c,resume=r)
        isave.save()
    return render(request,'ithank.html')
#%ADD A, FORM IN CONSULT
def payment(request):
    return render(request,'pay.html')
def payment_form(request):
    return render(request,'payform.html')