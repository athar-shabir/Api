from django import forms

class usersForm(forms.Form):
    num1 = forms.CharField(label="Enter the Number 1:",required=False,widget=forms.PasswordInput)
    num2 = forms.CharField(label="Enter the Number 2:",required=False,widget=forms.Textarea)
    num3 = forms.CharField(label="Enter the Number 3:",widget=forms.TextInput(attrs={'class':"form-control col-md-4"}))

# class logIn(forms.forms):
#     user = forms.CharField(label="User Name:")
#     password = forms.CharField(label="Password:")