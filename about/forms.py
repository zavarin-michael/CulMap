from django import forms


class CommentForm(forms.Form):
    User_name = forms.TextInput()
    Comment = forms.TextInput()