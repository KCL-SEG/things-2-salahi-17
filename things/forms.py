from django import forms

# Create your forms here.

class ThingForm(forms.Form):
    name = forms.CharField(label='name', max_length = 30)
    description = forms.CharField(label='Textarea', max_length = 120)
    quantity = forms.CharField(label='NumberInput', max_length = 50)