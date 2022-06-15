from django.shortcuts import render , HttpResponse , redirect
from home.models import Form
from datetime import date, datetime
from django.contrib.auth import authenticate,login , logout
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request, 'index.html') 
def consultation(request):       
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            address = request.POST.get('address')
            pain = request.POST.get('pain')
            bleeding = request.POST.get('bleeding')
            burning = request.POST.get('burning')
            itching = request.POST.get('itching')
            constipation = request.POST.get('constipation')
            prolepse = request.POST.get('prolepse')
            anus = request.POST.get('anus')
            othercom = request.POST.get('othercom')
            otherhis = request.POST.get('otherhis')
            digitalex = request.POST.get('digitalex')
            pathological = request.POST.get('pathological')
            diagnosis = request.POST.get('diagnosis')
            anesthesia = request.POST.get('anesthesia')
            estimate = request.POST.get('estimate')
            
            #---- Check data for not selected options ---------edited by @zk
            if (pain is None):
                pain="NIL"
            
            if (bleeding is None):
                bleeding="NIL"
            
            if (burning is None):
                burning="NIL"
            
            if (itching is None):
                itching="NIL"    
            
            if (constipation is None):
                constipation="NIL"    
            
            if (prolepse is None):
                prolepse="NIL"
            
            if (anus is None):
                anus="NIL"    
            
            if (othercom is None):
                othercom="NIL"

            if (digitalex is None):
                digitalex="NIL"
            
            if (pathological == ""):
                pathological="NIL"
            
            if (otherhis == ""):
                otherhis="NIL"
            
            if (diagnosis is None):
                diagnosis="NIL"
                
            if (anesthesia is None):
                anesthesia="NIL"

            if (estimate is None):
                estimate="NIL"

                
            consultation = Form(name=name, gender=gender, address=address , phone=phone, age=age, 
             pain=pain, bleeding=bleeding, burning=burning, itching=itching, constipation=constipation, 
             prolepse=prolepse, anus=anus, othercom=othercom, otherhis=otherhis, digitalex=digitalex,pathological=pathological, diagnosis=diagnosis , anesthesia=anesthesia, estimate=estimate,
             )
            
            consultation.save()
    
            messages.success(request, 'Your message has been sent !')
            return redirect('/dashboard')

        
        return render(request, 'consultation.html',{'date':datetime.today()})
        


def report(request):
    data= Form.objects.all()
    return render(request, 'report.html' ,{"mess":data} )

def handlesignup(request):
    if request.method =='POST':
        # GEt post parameter
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']


        # check for errorneous inputs
        if len(username) > 10:
            messages.error(request, 'Username must be under 10 characters')
            return redirect('/signup')
        if not username.isalnum():
             messages.error(request, 'Username should only contains numbers and letters')
             return redirect('/signup')
        
        if User.objects.filter(email=email).exists():
            messages.warning(request,'email is already exists')
            return redirect('/signup')
        
        if User.objects.filter(username=username).exists():
            messages.warning(request,'username is already exists')
            return redirect('/signup')
        
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'Your account created succesfully.')
        return redirect('/login')

        #createing user

        

    return render(request, 'register.html')

def handlelogin(request):
    if request.method =='POST':
        loginusername = request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user = authenticate( username= loginusername, password= loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'Succesfully logged In')
            return redirect('home')
        
        else:
            messages.error(request, 'Invalid Credentials , please try again')
            return redirect('/login')


    return render( request,'login.html')

def handlelogout(request):
    logout(request)
    messages.success(request, 'successfully logged out')
    return redirect('/login')  
        
    
    
    
