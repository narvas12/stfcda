from django import forms
from .models import Journalfiles, Nomination

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
        fields = ['Journal', 'title']