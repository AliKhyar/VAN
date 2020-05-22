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
        attrs={"type":"text", "required":"", "placeholder":"Please input your project duration", "value":"", "name":"name", "class":"txt"}
        )
    )
    #end = forms.CharField(label='End at ')
    cfy = forms.CharField(label='',
        widget=forms.TextInput(
        attrs={"type":"text", "required":"", "placeholder":"Please input your project cash flow/year", "value":"", "name":"name", "class":"txt"}
        )
    )
    taux = forms.CharField(label='',
        widget=forms.TextInput(
        attrs={"type":"text", "required":"", "placeholder":"Please input your project 'taux d actualisation'", "value":"", "name":"name", "class":"txt"}
        )
    )