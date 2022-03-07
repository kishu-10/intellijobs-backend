from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from jobs.forms import CategoryForm
from jobs.serializers import *
from rest_framework import status
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages


# Create your views here.

class DashboardJobCategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("dashboard:category_list")
    template_name = "job-category/category-create.html"

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(
            self.request, f"{name} created successfully.")
        super().form_valid(form)
        return HttpResponseRedirect(self.success_url)


class DashboardJobCategoryListView(ListView):
    model = Category
    template_name = "job-category/category-list.html"
    context_object_name = "category_list"


class DashboardJobCategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "job-category/category-update.html"
    context_object_name = "category"
    success_url = reverse_lazy("dashboard:category_list")

    def form_valid(self, form):
        messages.success(self.request, f"{self.object.name} updated successfully.")
        super().form_valid(form)
        return HttpResponseRedirect(self.success_url)


class DashboardJobCategoryDeleteView(DeleteView):
    model = Category
    form_class = CategoryForm
    context_object_name = "category"
    success_url = reverse_lazy("dashboard:category_list")

    def form_valid(self, form):
        messages.success(
            self.request, f"{self.object.name} deleted successfully.")
        super().form_valid(form)
        return HttpResponseRedirect(self.success_url)


class JobListView(ListAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.filter(
        is_active=True, deadline__gte=date.today()).order_by('-id')

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        print(category)
        if category:
            queryset = Job.objects.filter(
                is_active=True, category=category, deadline__gte=date.today()).order_by('-created_at')
        else:
            queryset = Job.objects.filter(
                is_active=True, deadline__gte=date.today()).order_by('-created_at')

        return queryset


class CategoriesListView(APIView):

    def get(self, request):
        """API to fetch all the Job Categories"""
        categories = Category.objects.filter(is_active=True)
        serializer = CategorySerializer(
            categories, many=True, context={'request': request})
        return Response(serializer.data)


class JobDetailView(APIView):

    def get(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)
        except:
            return Response([],
                            status=status.HTTP_400_BAD_REQUEST
                            )
        serializer = JobDetailSerializer(job, context={'request': request})
        return Response({'job_detail': serializer.data})


class CategoryCreateView(APIView):

    def post(self, request):
        serializer = JobCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
