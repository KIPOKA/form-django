from django import forms
from .models import Snippet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'name',
            'email',
            Submit('submit', 'Submit', css_class='btn-succes')
        )


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('name', 'email')
