from django.urls import path
from employee import views

urlpatterns=[
    path("signup",views.SignupView.as_view(),name="signup"),
    path("signin",views.SigninView.as_view(),name="signin"),
    path("logout",views.sign_out,name="signout"),
    path("jobs/post",views.PostJobs.as_view(),name="postjobs"),
    path("jobs/all",views.ListJobs.as_view(),name="listjobs"),
    path("jobs/update/<int:id>",views.UpdateJob.as_view(),name="updatejob"),
    path("jobs/delete/<int:id>",views.DeleteJobs.as_view(),name="deletejob"),
    path("jobs/application/all",views.ViewApllications.as_view(),name="viewapplications"),
    path("jobs/application/<int:id>",views.JobApplications.as_view(),name="jobapplications"),
    path("jobs/application/approve/<int:id>",views.applicationaccept,name="approveapplication"),
    path("jobs/application/reject/<int:id>", views.applicationreject, name="rejectapplication"),
]