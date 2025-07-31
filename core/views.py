from django.http import HttpResponse
from django.contrib.auth import get_user_model
import os


def criar_superusuario_secreto(request):
    User = get_user_model()
    username = os.environ.get('ADMIN_USER')
    email = os.environ.get('ADMIN_EMAIL')
    password = os.environ.get('ADMIN_PASSWORD')

    if not all([username, email, password]):
        return HttpResponse("As variáveis de ambiente ADMIN_USER, ADMIN_EMAIL e ADMIN_PASSWORD não foram definidas.", status=500)

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        return HttpResponse("<h1>Superusuário criado com sucesso!</h1><p>Agora você pode apagar esta rota e a view.</p>")
    else:
        return HttpResponse("<h1>Superusuário já existe.</h1>")
