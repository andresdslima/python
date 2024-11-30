from rest_framework import generics
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Project, Tag
from .forms import CreateProjectForm
from .serializers import ProjectSerializer


class HomeView(View):
    def get(self, request):
        projects = Project.objects.all()
        tags = Tag.objects.all()
        return render(request, "home.html", {"projects": projects, "tags": tags})


class ContactView(View):
    def get(self, request):
        return render(request, "contact.html")


class ProjectView(View):
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        return render(request, "project.html", {"project": project})


class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer

    # if needed to filter by tag_id
    def get_queryset(self):
        queryset = Project.objects.all()
        tag = self.request.query_params.get("tag")
        if tag:
            queryset = queryset.filter(tags__in=tag)
        return queryset


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectCreate(View):
    def get(self, request):
        form = CreateProjectForm()
        return render(request, "project_create.html", {"form": form})

    def post(self, request):
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect("project", pk=project.pk)
        return render(request, "project_create.html", {"form": form})


class ProjectDelete(View):
    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        if project:
            project.delete()
            return redirect("home")
        error_message = "There was an error while trying to delete this project"
        return render(
            request,
            "project.html",
            {"project": project, "error_message": error_message},
        )


class ProjectUpdate(View):
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        form = CreateProjectForm(instance=project)
        return render(
            request, "project_update.html", {"form": form, "project": project}
        )

    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        form = CreateProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save()
            return redirect("project", pk=project.pk)
        error_message = "Invalid form data"
        return render(
            request,
            "project_update.html",
            {"form": form, "project": project, "error_message": error_message},
        )
