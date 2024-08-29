from django import forms

from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ('firstname', 'lastname', 'email', 'phone', 'enquiry', 'image')

    email = forms.EmailField(
            label='Email', max_length=200, widget=forms.EmailInput(
                attrs={'class': 'form-control mb-3', 'id': 'form-email', 'style': 'width:300px'}))

    phone = forms.CharField(
            label='Phone Number', min_length=8, max_length=8, widget=forms.TextInput(
                attrs={'class': 'form-control mb-3', 'placeholder': '+65', 'id': 'form-phone', 'style': 'width:300px'}))

    firstname = forms.CharField(
        label='First name', max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'id': 'form-firstname', 'style': 'width:300px'}))
    
    lastname = forms.CharField(
        label='Last name', max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'id': 'form-lastname', 'style': 'width:300px'}))

    enquiry = forms.CharField(
        label='Enquiry', widget=forms.Textarea(
            attrs={'class': 'form-control mb-3', 'id': 'form-enquiry'}))

    image = forms.ImageField(
        label='Image inspiration', required=False, widget=forms.ClearableFileInput(
            attrs={'class': 'form-control mb-3', 'id': 'form-image'}))
