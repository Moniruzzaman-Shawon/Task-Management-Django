from django import forms 

class TaskForm(forms.Form):
    title = forms.CharField(max_length=250, label="Task Title")
    description = forms.CharField(widget=forms.Textarea, label='Task Description')
    due_date = forms.DateField(widget=forms.SelectDateWidget, label='Due Date')
    assigned_to = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple
        )
    
    def __init__(self, *args, **kwargs):
        employees = kwargs.pop("employees", [])
        super().__init__(*args, **kwargs) # * for unpack
# tasks/forms.py

class StyledFormMixin:
    def add_form_control_class(self):
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
