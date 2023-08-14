from django import forms

class createNewTask(forms.Form):
    title = forms.CharField(label="Task title", max_length=200)
    description = forms.CharField(label="Task descriptión", widget=forms.Textarea)