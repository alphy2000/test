"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('home',views.adindex,name="home"),
    path('ind',views.industrydetails,name="ind"),
    path('deleteind/<wal>',views.deleteind,name="deleteind"),
    path('addind',views.addind,name="addind"),
    path('search',views.searchfn,name="search"),

    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('logout',views.logout,name="logout"),

    path('jobs',views.viewjobs,name="jobs"),
    path('adjobdetail/<val>',views.adjobdetail,name="adjobdetail"),

    path('myjobs',views.myjobs,name="myjobs"),
    path('jobdetail/<val>',views.jobdetail,name="jobdetail"),

    path('post',views.postjob,name="post"),
    path('addcompany',views.addcompany,name="addcompany"),
    path('addjob',views.addjob,name="addjob"),
    path('editjob/<wal>',views.editjob,name="editjob"),
    path('editjob/editjob2/<wal>',views.editjob2,name="editjob2"),
    path('deletejob/<wal>',views.deletejob,name="deletejob"),



    path('test', views.test, name='test'),
    path('check_email', views.check_email, name='check_email'),

    path('get-items/', views.get_items, name='get_items'),
    path('get-jobs/', views.get_jobs_by_company, name='get_jobs_by_company'),

    
]
