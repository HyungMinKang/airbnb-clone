from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))

        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


# ModelForm 일일이 프로그래머가 필드를 설계할 필요없이 모델에서 갖다쓸 수 있게 해줌
class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email")

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password1 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("Password Error")
        else:
            try:
                password_validation.validate_password(password1, self.instance)
                return password
            except forms.ValidationError as error:
                self.add_error("password", error)

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.set_password(password)
        user.save()

