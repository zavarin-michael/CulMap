from django import forms


class CommentForm(forms.Form):
    username = forms.CharField(label=u'Username', widget=forms.TextInput(attrs={
        'size': 50
    }))
    comment = forms.CharField(label=u'Comment', widget=forms.Textarea(attrs={
        'size': 50
    }))

    id_mark = forms.IntegerField()