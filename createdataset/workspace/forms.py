from django import forms

class PhotoForm(forms.ModelForm):
    photo = forms.ImageField()
    class Meta:
        model = Object
        fields = [""]