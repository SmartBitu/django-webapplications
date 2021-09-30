from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from datetime import datetime
from django.contrib import messages
from home.models import Product, Contact, Service, Testimonials, Subscribe, UnicafeProduct
from math import ceil
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import string, random

# Create your views here.
def index(request):
    testimonials = Testimonials.objects.all()
    params = {'testimonials': testimonials}
    if 'session_timer' in request.session:
        request.session.modified = True
        
    
        
    # if request.method == "POST":
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     phone = request.POST.get('phone')
    #     subject = request.POST.get('subject')
    #     message = request.POST.get('message')
    #     contact = Contact(con_name=name, con_email=email, con_phone=phone, con_subject=subject, con_message=message, con_datetime=datetime.today())
    #     contact.save()

    return render(request, 'index.html', params)

def subscribe(request):
    if 'session_timer' in request.session:
        request.session.modified = True
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST.get('name','')
        mobno = request.POST.get('mobno','')
        if(email and name and mobno):
            subs = Subscribe(subs_name=name, subs_mobileno=mobno, subs_email=email, subs_datetime=datetime.today())
            subs.save()
            messages.success(request, 'Thank you for Contacting Us')
            return redirect('https://tel:9820188508')
        elif email:
            name = 'subscriber'
            subs = Subscribe(subs_name=name, subs_email=email, subs_datetime=datetime.today())
            subs.save()
            messages.success(request, 'Thank you for Subscribing')
            return redirect('home')
        else:
            messages.warning(request, 'Please fill up all fields')
            return redirect('home')
    else:
        return HttpResponseNotFound('<h1>404 - Not Found</h1>')
    

def style(request):
    if 'session_timer' in request.session:
        request.session.modified = True
    return render(request, 'index.html')

def services(request, myid):
    if 'session_timer' in request.session:
        request.session.modified = True
    service = Service.objects.filter(service_id=myid)
    params = {'service': service[0]}
    return render(request, 'services.html', params)

def indo(request):
    if 'session_timer' in request.session:
        request.session.modified = True
    return render(request, 'indo1.html')

def serviceshome(request):
    if 'session_timer' in request.session:
        request.session.modified = True
    allProds = Service.objects.all()
    params = {'service': allProds}
    return render(request, 'serviceshome.html', params)
    

def livestream(request):
    if 'session_timer' in request.session:
        request.session.modified = True
    return render(request, 'livestream.html')

def community(request):
    if 'session_timer' in request.session:
        request.session.modified = True
    return render(request, 'community.html')

def experiment(request):
    if 'session_timer' in request.session:
        request.session.modified = True
    return render(request, 'experiment.html')

def support(request):
    if 'session_timer' in request.session:
        request.session.modified = True
    return render(request, 'support.html')

def unicafe(request):
    if 'session_timer' in request.session:
        request.session.modified = True
    allProds = UnicafeProduct.objects.all()
    params = {'unicafepro': allProds}
    return render(request, 'unicafe.html', params)

def blog(request):
    if 'session_timer' in request.session:
        request.session.modified = True
    return render(request, 'blog.html')
    
def myaccount(request):
    if 'session_timer' in request.session:
        request.session.modified = True
        return render(request, 'myaccount.html')
    else :
        messages.warning(request, 'You are Not Logged In OR Your Session is Expired')
        return redirect('home')



def bloghome(request):
    if 'session_timer' in request.session:
        request.session.modified = True
    return render(request, 'bloghome.html')

def patenttechs(request):
    if 'session_timer' in request.session:
        request.session.modified = True
    return render(request, 'PatentTechs.html')

def franchise(request):
    if 'session_timer' in request.session:
        request.session.modified = True
    return render(request, 'Franchise.html')

# login and logout for site 
# Session value generation
def id_generator(size=30, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))   
def handleLogin(request):
    if request.method == 'POST':
        #get the post parameters
        #email == username
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpass)
        if user is not None:
            login(request, user)
            request.session['session_timer']=id_generator(20)
            #myuser = User.objects.get(username=loginusername)
            #myuser.session_id = request.session['session_timer']
            
            messages.success(request, "You are Successfully logged In")
            return redirect('home')
        else:
            messages.warning(request, "Invalid Credentials, Enter Correct Credentials.")
            return redirect('home')

    

def handleLogout(request):
    logout(request)
    request.session.flush()
    request.session.clear_expired()
    messages.success(request, "Successfully Logged Out")
    return redirect('home')


def productinfo(request):
    pro_id = request.GET.get('proid','')
    if pro_id:
        allProds= Product.objects.filter(pro_id=pro_id)
        params = {'product': allProds[0]}
        return render(request, 'productinfo.html', params)  
    else:
        return redirect('product')

      

def product(request):
    categories = Product.objects.order_by().values('pro_categary').distinct()
    # product = Product.objects.all()
    # n = len(product)
    # nslides = n//4 + ceil((n/4)-(n//4))
    category_name = request.GET.get('category','')
    if category_name:
        allProds= Product.objects.filter(pro_categary=category_name)
    else:
        allProds = Product.objects.all()

    params = {'product': allProds, 'category': categories}
    return render(request, 'product.html', params)

def handleSignup(request):
    if request.method == 'POST':
        #get the post parameters
        #email == username
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        mobno = request.POST['mobno']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        # check for errroneous inputs
        # username should be 10 characters
        if len(username) > 10:
            messages.warning(request, "Username must be under 10 characters")
            return redirect('home')
        
        # username should be alphanumaric
        if not username.isalnum():
            messages.warning(request, "Username should only contain letters and numbers")
            return redirect('home')
        # password should be match
        if password != cpassword:
            messages.warning(request, "Passwords do not Match")
            return redirect('home')
        #create user
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.last_name = mobno
        myuser.save()
        messages.success(request, "Your LifeShots Account Has Been Successfully Created")
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')

