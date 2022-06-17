from django import forms

class ContactPageForm(forms.Form):
    email = forms.EmailField(label="Your Email")
    name = forms.CharField(label="Your Name", max_length=20)
    number = forms.CharField(label="Your Number", max_length=12)
    message = forms.Textarea()


