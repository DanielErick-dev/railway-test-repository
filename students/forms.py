from .models import Students
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re


class StudentsForm(forms.ModelForm):
    cpf_validator = RegexValidator(
        r'^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$',
        'CPF inválido'
    )
    phone_number_validator = RegexValidator(
        r'^\d{2}9\d{8}$',
        'Telefone inválido'
    )

    class Meta:
        model = Students
        fields = ['name', 'lastname', 'cpf', 'sex', 'phone_number', 'date_of_birth']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control '}),
            'lastname': forms.TextInput(attrs={'class': 'form-control '}),
            'cpf': forms.TextInput(attrs={'class': 'form-control mask-cpf', 'placeholder': '999.999.999.99'}),
            'sex': forms.Select(attrs={'class': 'form-control '}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control mask-phone', 'placeholder': '(99) 9-9999-9999'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control ', 'type': 'date'}),
        }
        labels = {
            "name": "Nome",
            "lastname": "Sobrenome",
            "cpf": "CPF",
            "sex": "sexo",
            "phone_number": "Número de Telefone",
            "date_of_birth": "Data de Nascimento"
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        cpf_clean = re.sub(r'[^\d]', '', cpf)
        if len(cpf_clean) != 11:
            raise ValidationError('O campo CPF deve conter 11 digitos')
        try:
            self.cpf_validator(cpf_clean)
        except ValidationError as e:
            raise ValidationError(e.message)
        return cpf_clean

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        phone_number_clean = re.sub(r'[^\d]', '', phone_number)
        if len(phone_number_clean) != 11:
            raise ValidationError('O campo Telefone deve conter 11 digitos')
        try:
            self.phone_number_validator(phone_number_clean)
        except ValidationError as e:
            raise ValidationError(e.message)
        return phone_number_clean
