# Create your views here.
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from django.contrib.auth.models import User
from .models import Patient, Oxygen, Plasma
from django.template import Context, Engine, TemplateDoesNotExist, loader
from urllib.parse import quote

def index(request):

    # Authenticated users view their inbox
    if request.user.is_authenticated:
        plasma, oxygen, patient= fetchdata(request)
        if plasma is not None or oxygen is not None or patient is not None:
            return render(request, 'project/login_home.html',{
                "patients":patient,
                "oxygen":oxygen,
                "plasma":plasma
            })
        else:
            return render(request, 'project/login_home.html',{
                "message1":"No entry submitted by you till now."
            }  )

        

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login_details"))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        confirm=request.POST["c_password"]
        email=request.POST["email"]
        
        if username is None or username=='':
            return render(request,"project/register.html", {
                    "message": "Username not entered."
                })
        elif password is None or password=='':
            return render(request,"project/register.html", {
                    "message": "Password not entered"
                })
        elif confirm is None or confirm=='':
            return render(request,"project/register.html", {
                    "message": "Confirm Password not entered"
                })
        elif email is None or email=='':
            return render(request,"project/register.html", {
                    "message": "Email not entered"
                })
        if username is not None:
            if password!=confirm:
                return render(request,"project/register.html", {
                    "message": "Passwords must match."
                })
        
        
        try:
            user=User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError as e:
            return render(request, "project/register.html", {
                "message": "Username/Email address already exists."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "project/register.html")
    
  

def login_func(request):

    if request.method=="POST":
        
        username=request.POST.get('username')
        password=request.POST.get('password')   

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'project/login.html', {
                "message": "Invalid username and/or password."
            })
    
    else:
        return render(request, 'project/login.html')

#############################################################################
'''Function to Load list of Oxygen Suppliers'''

def load_pat(request):
    '''if request.method=="POST":'''
    #data = serializers.serialize('json', Patient.objects.all())
    # return render(request, 'templates/index.html', {'data': data})       
    patient= Patient.objects.all().order_by('-p_date')
    '''if request.method == "GET":
        return JsonResponse(patient.serialize())'''
    return render(request, 'project/patient.html',{
        "patient":patient
    })

def load_oxy(request):
    '''if request.method=="POST":'''
    #data = serializers.serialize('json', Patient.objects.all())
    # return render(request, 'templates/index.html', {'data': data})       
    oxygen= Oxygen.objects.all().order_by('-p_date')
    '''if request.method == "GET":
        return JsonResponse(patient.serialize())'''
    return render(request, 'project/oxygen.html',{
        "patient":oxygen
    })

def load_plas(request):
    '''if request.method=="POST":'''
    #data = serializers.serialize('json', Patient.objects.all())
    # return render(request, 'templates/index.html', {'data': data})       
    plasma= Plasma.objects.all().order_by('-p_date')
    '''if request.method == "GET":
        return JsonResponse(patient.serialize())'''
    return render(request, 'project/plasma.html',{
        "patient":plasma
    })

def FAQs(request):
    return render(request, 'project/FAQs.html')

def contactus(request):
    return render(request, 'project/contact.html')
def about(request):
    return render(request, 'project/about.html')
def bedsdelhi(request):
    return render(request, 'project/beds.html')
def delhiplasma(request):
    return render(request, 'project/delhiplasma.html')

#######################################################################

@csrf_exempt
@login_required
def fetchdata(request):
    plasma= Plasma.objects.filter(user=request.user)
    oxygen= Oxygen.objects.filter(user=request.user)
    patient= Patient.objects.filter(user=request.user)

    #if plasma is not None or oxygen is not None or patient is not None:
    return plasma, oxygen, patient
    
@csrf_exempt
@login_required
def deletedata(request,id, id_type):

    if id_type=="patient":
        patient= Patient.objects.filter(id=id)
        patient.delete()
    if id_type=="oxygen":
        oxy= Oxygen.objects.filter(id=id)
        oxy.delete()
    if id_type=="plasma":
        plas= Plasma.objects.filter(id=id)
        plas.delete()
    plasma, oxygen, patients= fetchdata(request)
    return render(request, 'project/login_home.html',{
                "patients":patients,
                "oxygen":oxygen,
                "plasma":plasma
            })

            
########################################################################       
'''Function to submit patient form'''

@csrf_exempt
@login_required
def patient_func(request):
        
    if request.method=="POST":
        pat_name=request.POST.get('your_name')
        pat_number=request.POST.get('your_number')
        pat_alt_numb=request.POST.get('your_alt_number')
        pat_locality=request.POST.get('your_locality')
        pat_city=request.POST.get('your_city')
        pat_state=request.POST.get('your_state')
        pat_remark=request.POST.get('your_remarks')

        if pat_name is None or pat_name=='':
            return render(request, 'project/login_home.html', {
            "message": "Please enter Name"
        })
        elif pat_number is None or pat_number=='':
            return render(request, 'project/login_home.html', {
            "message": "Please enter Contact Number"
        })
        elif pat_locality is None or pat_locality=='':
            return render(request, 'project/login_home.html', {
            "message": "Please enter Locality"
        })
        elif pat_city is None or pat_city=='':
            return render(request, 'project/login_home.html', {
            "message": "Please enter City"
        })
        elif pat_state is None or pat_state=='':
            return render(request, 'project/login_home.html', {
            "message": "Please enter State"
        })
        else:
            patient=Patient(user=request.user,p_name=pat_name, p_number=pat_number, p_alt_number=pat_alt_numb, p_locality=pat_locality, p_city=pat_city, p_state=pat_state, p_remark=pat_remark)

            patient.save()
            plasma, oxygen, patient1= fetchdata(request)
            return render(request, 'project/login_home.html', {
            
            "message": "Your Request has been posted Successfully. Please LOG OUT from your account.",
            "patients":patient1,
            "oxygen":oxygen,
            "plasma":plasma
        })
                        
    else:
        return render(request, 'project/login_home.html',{
            "message":"Some error occurred. Please try again!"
        })


##############################################################################



'''Function to call oxygen cylinder'''
@csrf_exempt
@login_required
def oxygen_func(request):
        
    if request.method=="POST":
        ox_name=request.POST.get('your_name')
        ox_company=request.POST.get('your_company')
        ox_number=request.POST.get('your_number')
        ox_alt_numb=request.POST.get('your_alt_number')
        ox_locality=request.POST.get('your_locality')
        ox_city=request.POST.get('your_city')
        ox_state=request.POST.get('your_state')
        ox_remark=request.POST.get('your_remarks')

        if ox_name is None or ox_name=='':
            return render(request, 'project/login_home.html', {
            "message": "Please enter Name"
        })
        elif ox_company is None or ox_company=='':
            return render(request, 'project/login_home.html', {
            "message": "Please enter Your Company Name"
        })
        elif ox_number is None or ox_number=='':
            return render(request, 'project/login_home.html', {
            "message": "Please enter Contact Number"
        })
        elif ox_locality is None or ox_locality=='':
            return render(request, 'project/login_home.html', {
            "message": "Please enter Locality"
        })
        elif ox_city is None or ox_city=='':
            return render(request, 'project/login_home.html', {
            "message": "Please enter City"
        })
        elif ox_state is None or ox_state=='':
            return render(request, 'project/login_home.html', {
            "message": "Please enter State"
        })
        else:
            oxygen=Oxygen(user=request.user, p_name=ox_name, p_company=ox_company, p_number=ox_number, p_alt_number=ox_alt_numb, p_locality=ox_locality, p_city=ox_city, p_state=ox_state, p_remark=ox_remark)
            oxygen.save()
            plasma, oxygen1, patient= fetchdata(request)
            return render(request, 'project/login_home.html', {
            
            "message": "Your Request has been posted Successfully.Please LOG OUT from your account.",
            "patients":patient,
                "oxygen":oxygen1,
                "plasma":plasma
        })
                        
    else:
        return render(request, 'project/login_home.html',{
            "message":"Some error occurred. Please try again!"
        })


############################################################################
@csrf_exempt
@login_required
def plasma_func(request):
        
    if request.method=="POST":
        pla_name=request.POST.get('your_name')
        pla_age=request.POST.get('your_age')
        pla_blood=request.POST.get('your_blood')
        pla_number=request.POST.get('your_number')
        pla_alt_numb=request.POST.get('your_alt_number')
        pla_locality=request.POST.get('your_locality')
        pla_city=request.POST.get('your_city')
        pla_state=request.POST.get('your_state')
        pla_remark=request.POST.get('your_remarks')

        if pla_name is None or pla_name=='':
            return render(request, 'project/login_home.html', {
            "message": "Please enter Name"
        })
        elif pla_age is None or pla_age=='':
            return render(request, 'project/login_home.html', {
            "message": "Please enter Your Age or below 18 years are not eligible"
        })
        elif pla_blood is None or pla_blood=='':
            return render(request, 'project/login_home.html', {
            "message": "Please enter your Blood Group"
        })
        elif pla_number is None or pla_number=='':
            return render(request, 'project/login_home.html', {
            "message": "Please enter Contact Number"
        })
        elif pla_locality is None or pla_locality=='':
            return render(request, 'project/login_home.html', {
            "message": "Please enter Locality"
        })
        elif pla_city is None or pla_city=='':
            return render(request, 'project/login_home.html', {
            "message": "Please enter City"
        })
        elif pla_state is None or pla_state=='':
            return render(request, 'project/login_home.html', {
            "message": "Please enter State"
        })
        else:
            plasma=Plasma(user=request.user,p_name=pla_name, p_age=pla_age, p_blood=pla_blood, p_number=pla_number, p_alt_number=pla_alt_numb, p_locality=pla_locality, p_city=pla_city, p_state=pla_state, p_remark=pla_remark)
            plasma.save()
            plasma1, oxygen, patient= fetchdata(request)
            return render(request, 'project/login_home.html', {
            
            "message": "Your Request has been posted Successfully. Please LOG OUT from your account.",
            "patients":patient,
            "oxygen":oxygen,
            "plasma":plasma1
        })
                        
    else:
        return render(request, 'project/login_home.html',{
            "message":"Some error occurred. Please try again!"
        })

###################################################################################

'''ERROR_404_TEMPLATE_NAME = '404.html'

ERROR_PAGE_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <title>%(title)s</title>
</head>
<body>
  <h1>%(title)s</h1><p>%(details)s</p>
</body>
</html>
"""
@requires_csrf_token
def page_not_found(request, exception, template_name=ERROR_404_TEMPLATE_NAME):
    """
    Default 404 handler.

    Templates: :template:`404.html`
    Context:
        request_path
            The path of the requested URL (e.g., '/app/pages/bad_page/'). It's
            quoted to prevent a content injection attack.
        exception
            The message from the exception which triggered the 404 (if one was
            supplied), or the exception class name
    """
    exception_repr = exception.__class__.__name__
    # Try to get an "interesting" exception message, if any (and not the ugly
    # Resolver404 dictionary)
    try:
        message = exception.args[0]
    except (AttributeError, IndexError):
        pass
    else:
        if isinstance(message, str):
            exception_repr = message
    context = {
        'request_path': quote(request.path),
        'exception': exception_repr,
    }
    try:
        template = loader.get_template(template_name)
        body = template.render(context, request)
        content_type = None             # Django will use DEFAULT_CONTENT_TYPE
    except TemplateDoesNotExist:
        if template_name != ERROR_404_TEMPLATE_NAME:
            # Reraise if it's a missing custom template.
            raise
        template = Engine().from_string(
            '<h1>Not Found</h1>'
            '<p>The requested resource was not found on this server.</p>')
        body = template.render(Context(context))
        content_type = 'text/html'
    return HttpResponseNotFound(body, content_type=content_type)
    '''
def error_404(request, exception):
    return render(request,'project/404.html')


