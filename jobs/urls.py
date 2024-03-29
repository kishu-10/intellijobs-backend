from django.conf.urls import url
from django.urls import re_path
from django.urls.conf import path

from jobs.views import *

app_name = "jobs"

urlpatterns = [
    path('', JobListView.as_view(), name='job-list'),
    path('job-search/', JobSearchFilterView.as_view(), name='job-search'),
    path('detail/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('categories/', CategoriesListView.as_view(), name='job-category'),
    path('category/create/', CategoryCreateView.as_view(),
         name='job-category-create'),
    path('wishlist/add/', CreateJobWishListView.as_view(), name='job-wishlist-add'),
    path('wishlist/<uuid>/', GetJobWishListView.as_view(), name='job-wishlist'),
    path('apply/', JobApplicationCreateView.as_view(), name='job-apply'),
    path('applied-jobs/', GetAppliedJobsView.as_view(), name='applied-jobs'),

]
