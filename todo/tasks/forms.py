from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    """ Form for Task model """
    title = forms.CharField(label='Task', widget=forms.TextInput(
        attrs={'id': 'task-form-field',
               'class': 'form-control',
               'type': 'text'}
    ))
    complete = forms.BooleanField(label='Complete', required=False, widget=forms.CheckboxInput(
        attrs={'id': 'task-complete-check',
               'class': 'form-check-input'}
    ))

    class Meta:
        model = Task
        fields = '__all__'
