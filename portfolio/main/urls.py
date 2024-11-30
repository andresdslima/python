from django.urls import path
from .views import HomeView, ContactView, ProjectView, ProjectList, ProjectDetail, ProjectCreate, ProjectDelete, ProjectUpdate

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("home/", HomeView.as_view(), name="home"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("project/<int:pk>/", ProjectView.as_view(), name="project"),
    path("api/", ProjectList.as_view(), name="project_list"),
    path("api/<int:pk>/", ProjectDetail.as_view(), name="project_detail"),
    path("project/create/", ProjectCreate.as_view(), name="project_create"),
    path("project/delete/<int:pk>/", ProjectDelete.as_view(), name="project_delete"),
    path("project/edit/<int:pk>/", ProjectUpdate.as_view(), name="project_update"),
]
