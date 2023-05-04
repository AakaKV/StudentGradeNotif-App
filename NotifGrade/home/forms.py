from django import forms 

class CreateNewAssignment(forms.Form):
    name = forms.CharField(label ="Name", max_length=200)
    description = forms.CharField(label="Description", max_length=200)