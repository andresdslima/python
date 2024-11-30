from django import forms
from .models import Project


class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "tags", "link"]
        widgets = {
            "tags": forms.CheckboxSelectMultiple,
            "link": forms.URLInput(
                attrs={"placeholder": "Project link", "class": "form-control"}
            ),
            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Project description",
                    "class": "form-control",
                }
            ),
            "title": forms.TextInput(
                attrs={"placeholder": "Project title", "class": "form-control"}
            ),
        }
