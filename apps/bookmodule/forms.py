from django import forms
from .models import Task
from .models import CheckList

class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task 
        fields = ['title', 'deadline', 'Priority','State','description']

    title = forms.CharField(
        max_length=50,
        required=True,
        label='Title:',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter the title here',
                'id':'title',
            }
        )
    )
    deadline = forms.DateTimeField(
        required=True,
        label='Deadline:',
        widget= DateTimePickerInput()
    )

    Priority = forms.CharField(
        max_length = 50,
        required=True,
        label='Priority:',
        widget=forms.Select(
            attrs={
                'id':'title'
            }
            ,choices=[
                ('low','Low'),
                ('high','High'),
                ('normal','Normal')
            ]
        )
    )

    State = forms.CharField(
        max_length=50,
        required=True,
        label='State:',
        widget=forms.Select(
            attrs={
                'id':'state'
            }
            ,choices=[
                ('toDo','To Do'),
                ('inProgress','In Progress'),
                ('done','Done')
            ]
        )
    )
    
    description = forms.CharField(
        max_length=500,
        required=True,
        label='Description:',
        widget=forms.Textarea(
            attrs={
                "rows": "10",
                'cols':'30',
                'maxlength':'500'
            }
        )
    )

class CheckListForm(forms.ModelForm):
    class Meta:
        model = CheckList 
        fields = ['title', 'description','done']

    title = forms.CharField(
        max_length=50,
        required=True,
        label='Title:',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter the title here',
                'id':'title',
            }
        )
    )
    
    description = forms.CharField(
        max_length=200,
        required=True,
        label='Description:',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter the description here',
                'id':'description',
            }
        )
    )
    
    done = forms.CharField(
        max_length=50,
        required=True,
        label='done? ',
        widget=forms.Select(
            attrs={
                'id':'done'
            }
            ,choices=[
                ('0','No'),
                ('1','Done')
            ]
        )
    )
    