from django.db import models

# Create your models here.

# -------------------------------- USER TABLE -------------------------------

class usersignup(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'
    

# -------------------------------- COMPANY TABLE -------------------------------

class industry(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'
        
    
class company(models.Model):
    userdet = models.ForeignKey(usersignup,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sector = models.ForeignKey(industry,on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    person = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    whatsapp = models.CharField(max_length=15,null=True)

    def __str__(self) -> str:
        return f'{self.name}'
    

# -------------------------------- JOB TABLE -------------------------------

class job(models.Model):
    companyname = models.ForeignKey(company,on_delete=models.CASCADE)
    name = models.CharField(max_length=100) 
    number = models.IntegerField()
    description = models.CharField(max_length=5000)
    location = models.CharField(max_length=500)
    tp = (
        ('Full Time','Full Time'),
        ('Part Time','Part Time'),
        ('Contract','Contract')
    )
    jobtype = models.CharField(max_length=1000,choices=tp,default='Full Time')

    hours = models.IntegerField()
    days = models.IntegerField()
    minsalary = models.CharField(max_length=15)
    maxsalary = models.CharField(max_length=15)
    qualification = models.CharField(max_length=500)
    skills = models.CharField(max_length=500)
    experience = models.IntegerField()

    g = (
        ('Female','Female'),
        ('Male','Male'),
        ('Any','Any')
    )
    gender = models.CharField(max_length=1000,choices=g,default='Any')

    minage = models.IntegerField(null=True)
    maxage = models.IntegerField(null=True)

    ap = (
        ('Pending','Pending'),
        ('Approved','Approved')
    )
    approval = models.CharField(max_length=1000,choices=ap,default='Pending')

    def __str__(self) -> str:
        return f'{self.name}'




        