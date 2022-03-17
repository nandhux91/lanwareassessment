from django.urls import path
from candidate import views

urlpatterns=[
    path("",views.ListJobs.as_view(),name="cust_jobs"),
    path("candidate/jobs/apply/<int:id>",views.JobApply.as_view(),name="jobapply"),
    path("candidate/jobs/view/<int:id>",views.JobDetailView.as_view(),name="jobdetail"),
    path("candidate/applications/all",views.ViewApplications.as_view(),name="myapplications")

]
