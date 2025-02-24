from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages 


# Create your views here.

def index(r):
    return render(r,'index.html')

def adindex(r):
    return render(r,'adminpage/index.html')

def industrydetails(r):
    l = industry.objects.all()
    return render(r,'adminpage/industry.html',{'l':l})

def viewjobs(r):
    l=job.objects.all()
    categories = company.objects.all()
    return render(r,'adminpage/jobs.html',{'l':l,'categories': categories})

def adjobdetail(r,val):
    n = job.objects.filter(id=val).first()
    return render(r,'adminpage/job_details.html',{'n':n})

def deleteind(a2,wal):
    obj = industry.objects.filter(id=wal).first()
    obj.delete()
    return redirect(industrydetails)

def searchfn(r):
    if r.method == 'POST':
        sr = r.POST.get('sr')
        print(sr)
        l = job.objects.filter(name__icontains = sr)
        return render(r,'adminpage/jobs.html',{'l':l})


def addind(r):
    if 'id' in r.session:
        if r.method == 'POST':
            n = r.POST.get('name')
            obj = industry.objects.create(name=n)
            obj.save()
            return redirect(industrydetails)
        return render(r,'adminpage/industry.html')
    return redirect(login)

# ------------------- SIGNUP/LOGIN/LOGOUT FUNCTIONS STARTS ---------------------

# User Login

def login(l1):
    if l1.method=='POST':
        e = l1.POST.get('email')
        p =  l1.POST.get('password')
        if e=='admin'and p=='1234':
            l1.session['id'] = ['admin']
            return redirect(adindex)

        elif usersignup.objects.filter(email=e).exists():
            usr = usersignup.objects.filter(email=e).first()
            if usr.password == p:
                l1.session['id'] = [usr.id]
                return redirect(index)
            else:
                messages.info(l1,'Incorrect Password',extra_tags="login")
                return redirect(login)

        else:
            messages.info(l1,'Username not found',extra_tags="login")
            return redirect(login)
        
    return render(l1,'login.html')

# Logout page

def logout(l3):
    if 'id' in l3.session:
        l3.session.flush()
        return redirect(index)
    return render(l3,'index.html')


# User Signup

def signup(l2):
    if l2.method == 'POST':
        n = l2.POST.get('name')
        e = l2.POST.get('email')
        ph = l2.POST.get('phone')
        d = l2.POST.get('dob')
        p = l2.POST.get('password')
        p2 = l2.POST.get('repassword')
        print(ph)
        if p == p2: 
            if usersignup.objects.filter(email=e).exists():
                messages.info(l2,"Email already exists",extra_tags="signup")
                return redirect(signup)  
            else:
                val=usersignup.objects.create(name=n,email=e,phone=ph,dob=d,password=p)
                val.save()  
                return redirect(login) 
        else:
            messages.info(l2,"Password doesn't match",extra_tags="signup")
            return redirect(signup) 

    return render(l2,'login.html')

# ------------------- SIGNUP/LOGIN/LOGOUT FUNCTIONS ENDS ---------------------
##########################




def myjobs(r):
    if 'id' in r.session:
        se = r.session.get('id')
        val = se[0]
        usr = usersignup.objects.get(id = val)
        c = company.objects.filter(userdet=usr).first()
        l=job.objects.filter(companyname=c).all()
    return render(r,'jobs.html',{'l':l})

def jobdetail(r,val):
    n = job.objects.filter(id=val).first()
    return render(r,'job_details.html',{'n':n})

def postjob(r):
    if 'id' in r.session:
        se = r.session.get('id')
        val = se[0]
        usr = usersignup.objects.get(id = val)
        c = company.objects.all()
        m = industry.objects.all()
        # if c:
        return render(r,'postjob.html',{'c':c})
        # else:
        #     return render(r,'addcompany.html',{'m':m})
    return render(r,'login.html')

def addcompany(r):
    if 'id' in r.session:
        se = r.session.get('id')
        val = se[0]
        usr = usersignup.objects.get(id = val)
        m = industry.objects.all()
        if r.method == 'POST':
            n = r.POST.get('name')
            s = r.POST.get('sector')
            ph = r.POST.get('phone')
            p = r.POST.get('person')
            d = r.POST.get('designation')
            e = r.POST.get('email')
            w = r.POST.get('whatsapp')
            print(e)
            sect = industry.objects.filter(name=s).first()
            obj = company.objects.create(userdet=usr,name=n,sector=sect,phone=ph,person=p,designation=d,email=e,whatsapp=w)
            obj.save()
            return redirect(postjob)
        return render(r,'addcompany.html',{'m':m})
    return redirect(login)
    
def addjob(r):
    if 'id' in r.session:
        se = r.session.get('id')
        val = se[0]
        usr = usersignup.objects.get(id = val)
        if r.method == 'POST':
            name = r.POST.get('name')
            comp = r.POST.get('company')
            c = company.objects.filter(id=comp).first()
            number = r.POST.get('number')
            description = r.POST.get('description')
            location = r.POST.get('location')
            jobtype = r.POST.get('jobtype')
            hours = r.POST.get('hours')
            days = r.POST.get('days')
            minsalary = r.POST.get('minsalary')
            maxsalary = r.POST.get('maxsalary')
            qualification = r.POST.get('qualification')
            skills = r.POST.get('skills')
            experience = r.POST.get('experience')
            gender = r.POST.get('gender')
            minage = r.POST.get('minage')
            maxage = r.POST.get('maxage')
            obj = job.objects.create(companyname=c,name=name,number=number,description=description,location=location,jobtype=jobtype,hours=hours,days=days,minsalary=minsalary,maxsalary=maxsalary,qualification=qualification,skills=skills,experience=experience,gender=gender,minage=minage,maxage=maxage)
            obj.save()
            return redirect(postjob)
        return render(r,'addcompany.html')
    
def editjob(a2,wal):
    obj = job.objects.filter(id=wal).first()
    return render(a2,'editjob.html',{'obj':obj})
    
def editjob2(r,wal):
    obj = job.objects.get(id=wal)
    if r.method=='POST':
        obj.name=r.POST.get('name')
        obj.number = r.POST.get('number')
        obj.description = r.POST.get('description')
        obj.location = r.POST.get('location')
        obj.jobtype = r.POST.get('jobtype')
        obj.hours = r.POST.get('hours')
        obj.days = r.POST.get('days')
        obj.minsalary = r.POST.get('minsalary')
        obj.maxsalary = r.POST.get('maxsalary')
        obj.qualification = r.POST.get('qualification')
        obj.skills = r.POST.get('skills')
        obj.experience = r.POST.get('experience')
        obj.gender = r.POST.get('gender')
        obj.minage = r.POST.get('minage')
        obj.maxage = r.POST.get('maxage')
        obj.save()
        return redirect(myjobs)
    return render(r,'myadmin/edit-product.html',{'obj':obj})

def deletejob(a2,wal):
    obj = job.objects.filter(id=wal).first()
    obj.delete()
    return redirect(myjobs)




from django.http import JsonResponse

def test(r):
    return render(r,'test.html')

#email check in registration using Ajax
def check_email(request):
    if request.method == "GET":
        email = request.GET.get('email', None)
        
        if email:
            if usersignup.objects.filter(email=email).exists():
                return JsonResponse({'exists': True})  
            else:
                return JsonResponse({'exists': False})  
        else:
            return JsonResponse({'error': 'No email provided'}, status=400)
        




def get_items(request):
    category_id = request.GET.get('category_id')
    c = company.objects.filter(id=category_id).first()
    items = job.objects.filter(companyname=c).values('name','location','jobtype')
    return JsonResponse({'items': list(items)})



def get_jobs_by_company(request):
    company_id = request.GET.get('company_id')
    if company_id == 'All':
        jobs = job.objects.all().values('id','name', 'location', 'jobtype')
        return JsonResponse({"jobs": list(jobs)})
    else:
        jobs = job.objects.filter(companyname=company_id).values('id','name', 'location', 'jobtype')
        return JsonResponse({"jobs": list(jobs)})