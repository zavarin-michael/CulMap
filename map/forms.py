from django import forms

class MarkForm(forms.Form):
    name = forms.CharField(label=u'Name', widget=forms.TextInput(attrs={
        'size': 50
    }))
    comment = forms.CharField(label=u'Comment', widget=forms.Textarea(attrs={
        'size': 50
    }))
    image = forms.ImageField(label=u'Image')
    position_y = forms.FloatField(label=u'y')
    position_x = forms.FloatField(label=u'x')
    type = forms.IntegerField()