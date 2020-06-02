from django import forms


class CommentForm(forms.Form):
    username = forms.CharField(label=u'Электронная почта', widget=forms.TextInput(attrs={
        'size': 50
    }))
    comment = forms.CharField(label=u'Электронная почта', widget=forms.TextInput(attrs={
        'size': 50
    }))