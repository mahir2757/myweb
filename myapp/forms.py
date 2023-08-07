from django import forms 
from myapp.models import ProjectDetail

class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectDetail
        fields = "__all__" 