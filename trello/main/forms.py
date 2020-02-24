from django import forms
from .models import Task

class AddTaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['article']
    performer = forms.BooleanField(initial=False, label='performer', label_suffix='', required=False)


class UpdateTaskForm(forms.ModelForm):
    
    class Meta:
        model=Task
        fields= ('article', 'performer', 'status')

class UpdateStatusForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['status']