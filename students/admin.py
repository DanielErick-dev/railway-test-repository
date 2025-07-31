from django.contrib import admin
from .models import Students


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'cpf', 'sex', 'phone_number', 'status', 'date_of_birth', 'expiration_date', )
    search_fields = ('name', 'cpf', )


admin.site.register(Students, StudentAdmin)
