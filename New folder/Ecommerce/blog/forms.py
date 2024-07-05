from django import forms

from .authentication_form import AuthenticationForm
from .models import Customer, Product, User

from blog.authentication_form import AuthenticationForm
class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ()


class ProductListModelForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()


# Login and register

# class LoginForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(max_length=255)
#
#     def clean_email(self):
#         email = self.data.get('email')
#         if not User.objects.filter(email=email).exists():
#             raise forms.ValidationError('Bunday email topilmadi')
#         return email
#
#     def clean_password(self):
#         email = self.cleaned_data.get('email')
#         password = self.data.get('password')
#         try:
#             user = User.objects.get(email=email)
#             if not user.check_password(password):
#                 raise forms.ValidationError('Parol xato')
#         except User.DoesNotExist:
#             raise forms.ValidationError(f'Bunday {email} mavjud emas')
#         return password


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField()
    password = forms.CharField(max_length=255)
    confirm_password = forms.CharField(max_length=255)

    def clean_email(self):
        email = self.data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'Bunday {email} allaqachon mavjud')
        return email

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Password did not match')

        return password


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
    from_email = forms.EmailField()
    to = forms.EmailField()


# from django.contrib.auth.forms import UserCreationForm
#
#
# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = Customer
#         fields = ('first_name',  'email', 'password', 'confirm_password')


class LoginForm(AuthenticationForm):
    email = forms.EmailField()
    password = forms.CharField(max_length=255)