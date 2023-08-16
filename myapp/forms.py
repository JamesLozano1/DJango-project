from django import forms
from .models import Project

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Task title", max_length=200)
    description = forms.CharField(label="Task descriptión", widget=forms.Textarea)


    # CHOICES = (('opcion 1', 'option 1'), ('option 2', 'option 2'))
    # project_id = forms.CharField(label='Project', widget=forms.Select(choices=CHOICES))

    CHOICES = Project.objects.all()
    project_id = forms.ModelChoiceField(label='Project', queryset=CHOICES)

class createNewProyect(forms.Form):
    name = forms.CharField(max_length=50, label='Ingrese el nombre del projecto')
