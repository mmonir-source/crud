from django import forms
from first_app import models

class MusicianForm(forms.ModelForm):
   first_name = forms.CharField(label="First Name")
   class Meta:
      model = models.Musician
      fields = "__all__"

class AlbumForm(forms.ModelForm):
   name = forms.CharField(label="Album Name")
   release_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
   class Meta:
      model = models.Album
      fields = "__all__"