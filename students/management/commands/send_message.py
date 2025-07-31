from django.core.management.base import BaseCommand
from students.models import Students
from clients.callmebot_service import CallMeBot
from students.messages import MESSAGE_TEMPLATE


class Command(BaseCommand):
    def handle(self, *args, **options):
        pending_students = Students.objects.filter(status='P')
        if pending_students:
            students_list = []
            for student in pending_students:
                students_list.append(
                    f"ALUNO: *{student.name.title()} {student.lastname.title()}*\n"
                    f"DATA DO VENCIMENTO: *{student.expiration_date.strftime('%d/%m/%Y')}*\n"
                )
            mensagem_final = MESSAGE_TEMPLATE.format(
                students_list='\n'.join(students_list)
            )
            callmebot = CallMeBot()
            callmebot.send_message(mensagem_final)
            print('mensagem enviada com sucesso')
        else:
            print('não há alunos pendentes, portanto não houve envio de mensagem')
