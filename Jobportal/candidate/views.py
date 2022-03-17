from django.shortcuts import render,redirect
from django.views.generic import View, ListView, CreateView,TemplateView,DeleteView,DetailView

from employee.models import Jobs
from .models import ApplicationModel
from .forms import ApplicationForm
from django.utils.decorators import method_decorator
from.decorators import sign_in_required
from django.contrib import messages
from employee.functions import handle_uploaded_file



# Create your views here.

class ListJobs(ListView):
    model = Jobs
    context_object_name = "jobs"
    template_name = "view_Jobs.html"

@method_decorator(sign_in_required,name="dispatch")
class JobApply(CreateView):
    model = ApplicationModel
    template_name = "job_application.html"
    form_class = ApplicationForm
    def post(self, request, *args, **kwargs):

        id=kwargs.get("id")
        form=ApplicationForm(request.POST,request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['resume'])
            user=request.user
            name=form.cleaned_data.get("name")
            phone=form.cleaned_data.get("phone")
            location=form.cleaned_data.get("location")
            qualification=form.cleaned_data.get("qualification")
            experience=form.cleaned_data.get("experience")
            resume=form.cleaned_data.get("resume")
            jobid=id
            job=Jobs.objects.get(id=id)
            Application=ApplicationModel(user=user,job=job,jobid=jobid,name=name,phone=phone,location=location,
                                         qualification=qualification,resume=resume,experience=experience
                                         )
            Application.save()
            return redirect("cust_jobs")

class JobDetailView(DetailView):
    model = Jobs
    template_name = "job_details.html"
    pk_url_kwarg = "id"
    context_object_name = "job"

@method_decorator(sign_in_required,name="dispatch")
class ViewApplications(ListView):
    model = ApplicationModel
    context_object_name = "apps"
    template_name = "view_my_applications.html"
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)







