from django import forms

from .models import Post
class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Sel a file',
        help_text='max. 42 megabytes'
    )
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('year', 'month', 'hotel_name','call_choices', 'docfile',  'operator', 'agent', 'ca4r', 'agu', 'aph','tyh','h90', 'nncb', 'cb30', 'avdda', 'asb', 'wby', 'hmpb', 'uim','daqr','qr', 'us', 'sqr5', 'ua', 'ta', 'un','comments_and_suggestions',)
