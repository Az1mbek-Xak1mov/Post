import re

from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.forms import Form
from django.forms.fields import CharField
from django.forms.models import ModelForm

from authenticate.models import User


class LoginForm(Form):
    country_code = CharField(max_length=5)
    phone_number = CharField(max_length=255)
    password = CharField(max_length=255)

    def clean(self):
        phone_number = self.cleaned_data.get("phone_number")
        phone_number = re.sub('\D' , "" , phone_number)
        country_code = self.cleaned_data.get("country_code")
        password = self.cleaned_data.get("password")
        query = User.objects.filter(phone_number=phone_number , country_code=country_code)
        if query.exists():
            user = query.first()
            if password == user.password:
                self.user = user
            else:
                raise ValidationError("password or phone number in correct")
        else:
            raise ValidationError("Not Found account")