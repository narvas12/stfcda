from django import forms
from .models import Journalfiles, Nomination, VolunteerApplication

class NominationForm(forms.ModelForm):
    class Meta:
        model = Nomination
        fields = ['member', 'is_nominated', 'n_reason']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set is_nominated as not required
        self.fields['is_nominated'].required = False




class JournalfilesForm(forms.ModelForm):
    class Meta:
        model = Journalfiles
        fields = ['Journal', 'title', 'version']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['version'].widget = forms.NumberInput(attrs={'min': 1, 'max': 100})  # Set min and max values as per your requirement
        
        
        
        
        
# class VolunteerApplicationForm(forms.ModelForm):
#     class Meta:
#         model = VolunteerApplication
#         fields = '__all__'

    
