from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Task title", max_length=200)
    description = forms.CharField(label="Task descriptión", widget=forms.Textarea)

class createNewProyect(forms.Form):
    name = forms.CharField(max_length=50, label='Ingrese el nombre del projecto')
