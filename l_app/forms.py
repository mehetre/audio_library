from django import forms
from .models import Song



#DataFlair
class SongCreate(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'
