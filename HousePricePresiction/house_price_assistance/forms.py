from django import forms

class HouseExamineForm(forms.Form):
    nickName = forms.CharField()
    phone = forms.CharField()
    Area = forms.CharField()
    city = forms.CharField()
    facility = forms.CharField(required=False)