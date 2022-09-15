from django.urls import path
from . import views

urlpatterns = [
    path("adverts/", views.JobPosting.as_view(), name="job-posting"),
    path("adverts/available/", views.available_adverts, name="available-posting"),
    path("adverts/<int:advert_id>/make-advert-unavailable/", views.make_advert_unavailable, name="make-post-unavailable"),
    path("adverts/<int:advert_id>/make-advert-available/", views.make_advert_available, name="make-post-available"),
    path("adverts/<int:advert_id>/", views.JobAdvertDetail.as_view(), name="job-advert-detail"),
    path("applications/", views.job_application, name="job-application"),
    path("applications/<int:application_id>/", views.JobApplicationDetail.as_view(), name="job-application-detail"),
    path("relate/<int:application_id>/", views.AdvertRelateApplication.as_view(), name="job-application-relate"),
]