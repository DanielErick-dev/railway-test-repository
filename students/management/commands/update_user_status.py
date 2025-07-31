from django.core.management.base import BaseCommand
from students.models import Students
from datetime import datetime, timedelta


class Command(BaseCommand):
    def handle(self, *args, **options):
        today = datetime.now().date()
        expiration_students = Students.objects.filter(
            expiration_date__lt=today,
            status='A'
        )
        for student in expiration_students:
            student.status = 'P'
            student.last_status_change = today
            student.save()
            self.stdout.write(f'Aluno {student.name} {student.lastname} atualizado para Pendente')
        limit_inactivity = today - timedelta(days=7)
        old_pending_students = Students.objects.filter(
            last_status_change__lte=limit_inactivity,
            status='P',
        )
        for student in old_pending_students:
            student.status = 'I'
            student.save()
            self.stdout.write(f'Aluno {student.name} {student.lastname} atualizado para Inativo')
