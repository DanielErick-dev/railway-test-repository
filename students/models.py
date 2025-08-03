from django.db import models
from django.utils import timezone


class Students(models.Model):
    SEX_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )
    STATUS = (
        ('A', 'Ativo'),
        ('P', 'Pendente'),
        ('I', 'Inativo')
    )
    name = models.CharField(max_length=200, verbose_name='nome')
    lastname = models.CharField(max_length=200, verbose_name='sobrenome')
    cpf = models.CharField(max_length=15, unique=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    phone_number = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField(verbose_name='data de nascimento')
    status = models.CharField(max_length=1, choices=STATUS, verbose_name='Status Do Aluno', default='A')
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField(null=True, blank=True)
    last_status_change = models.DateField(auto_now=True)

    class Meta:
        ordering = ['name', 'lastname']

    def __str__(self):
        return f"{self.name} {self.lastname}"

    @property
    def days_to_inactivity(self):
        if self.status != 'P':
            return None
        pendent_days = (timezone.now().date() - self.last_status_change).days
        return max(0, 7 - pendent_days)
