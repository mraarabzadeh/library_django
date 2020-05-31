from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from library.models import User, Book


class SignUpForm(forms.ModelForm):
    aggreament = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ['university_id', 'password', 'email']

    def clean_aggreament(self):
        if not self.cleaned_data['aggreament']:
            raise ValidationError('موافقت کن کونی')


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean_title(self):
        if Book.AllBook.filter(title=self.cleaned_data['title']).count() != 0:
            raise ValidationError('کتاب با این اسم موجود است')


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['university_id']


class NewSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields =['university_id', 'email',]


class SearchBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title']