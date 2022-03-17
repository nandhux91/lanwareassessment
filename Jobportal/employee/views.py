from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import View, ListView, CreateView,TemplateView,DeleteView,DetailView,UpdateView
from .forms import UserRegistrationForm,LoginForm,JobPostingForm,ApplicationProcessForm
from .models import Jobs
from django.urls import reverse_lazy
from candidate.models import ApplicationModel
from django.utils.decorators import method_decorator
from candidate.decorators import is_employer
from django.contrib import messages




from django.contrib.auth import authenticate, login, logout



# Create your views here.

class SignupView(View):
    def get(self,request,*args,**kwargs):
        form = UserRegistrationForm()
        context = {"form": form}
        return render(request,"signup.html",context)
    def post(self,request,*args,**kwargs):
        form=UserRegistrationForm(request.POST)

        if form.is_valid():
            messages.success(request, "Registration success")
            form.save()
            return redirect("signin")
        else:
            messages.error(request,"Registration failed")
            context = {"form": form}
            return render(request, "signup.html", context)

class SigninView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm
        context={"form":form}
        return render(request,"signin.html",context)
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                if request.user.role=='employer':
                    return redirect("listjobs")
                elif request.user.role == 'candidate':
                    return redirect("cust_jobs")
            else:
                context = {"form": form}
                return render(request, "signin.html", context)

def sign_out(request):
    logout(request)
    return redirect("signin")

@method_decorator(is_employer,name="dispatch")
class PostJobs(CreateView):
    model = Jobs
    template_name = "post_jobs.html"
    form_class = JobPostingForm
    def post(self, request, *args, **kwargs):
        form = JobPostingForm(request.POST)
        if form.is_valid():
            messages.success(request, "Job added successfully")
            user=request.user
            designation=form.cleaned_data.get("designation")
            company=form.cleaned_data.get("company")
            description=form.cleaned_data.get("description")
            location=form.cleaned_data.get("location")
            skills=form.cleaned_data.get("skills")
            salary=form.cleaned_data.get("salary")

            jobs=Jobs(user=user,designation=designation,company=company,description=description,
                      location=location,skills=skills,salary=salary,
                      )
            jobs.save()
            return redirect("postjobs")






#     def get(self,request,*args,**kwargs):
#         form=JobPostingForm()
#         context={"form":form}
#         return render(request,"post_jobs.html",context)
#     def post(self,request,*args,**kwargs):
#         form=JobPostingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("postjobs")
#         else:
#             context = {"form": form}
#             return render(request, "post_jobs.html", context)

@method_decorator(is_employer,name="dispatch")
class ListJobs(ListView):
    model = Jobs
    template_name = "list_jobs.html"
    context_object_name = "jobs"

@method_decorator(is_employer,name="dispatch")
class UpdateJob(UpdateView):
    model = Jobs
    pk_url_kwarg = "id"
    template_name = "update_job.html"
    form_class = JobPostingForm
    success_url = reverse_lazy("listjobs")

@method_decorator(is_employer,name="dispatch")
class DeleteJobs(DeleteView):
    model = Jobs
    success_url = reverse_lazy("listjobs")
    pk_url_kwarg = "id"
    template_name = "delete_job.html"
    # def get(self,request,*args,**kwargs):
    #     id=kwargs["id"]
    #     job=Jobs.objects.get(id=id)
    #     job.delete()
    #     return redirect("listjobs")

@method_decorator(is_employer,name="dispatch")
class ViewApllications(ListView):
    model = ApplicationModel
    context_object_name = "apps"
    template_name = "view_applications.html"
    # def post(self,request,*args,**kwargs):

@method_decorator(is_employer,name="dispatch")
class JobApplications(ListView):
    model = ApplicationModel
    context_object_name = "apps"
    template_name = "job_applications.html"
    def get(self,request,*args,**kwargs):
        jobid=kwargs.get("id")
        qs=self.model.objects.filter(jobid=jobid)
        context={"apps":qs}
        return render(request,self.template_name,context)



@method_decorator(is_employer,name="dispatch")
class ApplicationProcessView(UpdateView):
    model = ApplicationModel
    template_name = "process_application.html"
    form_class = ApplicationProcessForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("myapplications")

# @method_decorator(is_employer,name="dispatch")
@is_employer
def applicationaccept(request,*args,**kwargs):
    id=kwargs.get("id")
    application=ApplicationModel.objects.get(id=id)
    application.status="approved"
    application.save()
    messages.success(request, "Application approved")
    return redirect("listjobs")

# @method_decorator(is_employer,name="dispatch")
@is_employer
def applicationreject(request,*args,**kwargs):
    id=kwargs.get("id")
    application=ApplicationModel.objects.get(id=id)
    application.status="rejected"
    application.save()
    messages.error(request, "Application rejected")

    return redirect("listjobs")



