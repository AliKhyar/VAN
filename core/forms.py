from django import forms

class AddProduct(forms.Form):
    name = forms.CharField(max_length=100, label='',
    widget=forms.TextInput(
        attrs={"type":"text", "required":"", "placeholder":"Please input your project name", "value":"", "name":"name", "class":"txt"}
        )
    )
    description = forms.CharField(max_length=250, label='',
    widget=forms.TextInput(
        attrs={"placeholder":"Please input your project description", "value":"", "name":"name", "class":"form-control", "rows":5}
        )
    )
    duration = forms.DurationField(label='',
        widget=forms.TextInput(
        attrs={"type":"text", "required":"", "placeholder":"Please input your project duration by days", "value":"", "name":"name", "class":"txt"}
        )
    )
    capitale = forms.IntegerField(label='',
        widget=forms.TextInput(
        attrs={"type":"text", "required":"", "placeholder":"Please input your project capitale", "value":"", "name":"name", "class":"txt"}
        )
    )
    cfy = forms.IntegerField(label='',
        widget=forms.TextInput(
        attrs={"type":"text", "required":"", "placeholder":"Please input your project cash flow/year", "value":"", "name":"name", "class":"txt"}
        )
    )
    taux = forms.FloatField(label='',
        widget=forms.TextInput(
        attrs={"type":"text", "required":"", "placeholder":"taux d actualisation > 0 and < 1", "value":"", "name":"name", "class":"txt"}
        )
    )

    # def clean(self):
    #     cleaned_data = super().clean()
    #     taux = cleaned_data.get(taux)
    #     print(taux)
    #     if ((float(taux) > 1) or (float(taux) < 0)):
    #         raise forms.ValidationError(('taux must be between 0 and 1'))
    #     return cleaned_data
