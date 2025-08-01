# Academia Strong Fitness - Sistema de Gestão

<img width="1352" height="647" alt="image" src="https://github.com/user-attachments/assets/0e23a34f-7142-4aa2-a659-fa5815ed0c13" />


## 📖 Sobre o Projeto

O **Strong Fitness** é um sistema de software completo (Full-Stack) projetado para otimizar a gestão de alunos em uma academia. A aplicação automatiza tarefas administrativas, fornece relatórios e oferece uma interface de gerenciamento intuitiva.

---

## 🌟 Principais Funcionalidades

- **👤 Gestão Completa de Alunos (CRUD):** Cadastro, visualização, edição e exclusão de alunos.
- **🔄 Automação de Status:** O sistema altera o status do aluno para `ativo`, `pendente` ou `inativo` com base na data de vencimento da mensalidade, que é calculada automaticamente.
- **⏰ Verificação Diária Automatizada:** Um cron job é executado diariamente para verificar os vencimentos e atualizar os status, garantindo que os dados estejam sempre precisos.
- **🤖 Notificações via WhatsApp:** Integração com a API do CallMeBot para enviar um relatório diário com a lista de alunos pendentes, agilizando o processo de cobrança.
- **🔍 Busca e Filtragem Avançada:** A interface permite buscar alunos por nome ou CPF e visualizar listas separadas para alunos pendentes e inativos.
- **💳 Reativação de Matrícula Simplificada:** Um aluno pendente ou inativo pode ter sua matrícula renovada com um único clique, atualizando seu status e data de vencimento instantaneamente.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Propósito |
|---|---|
| **Python** | Linguagem principal do back-end |
| **Django & Django REST Framework** | Framework para construção da API RESTful |
| **HTML & CSS & JavaScript** | Construção da interface de usuário (front-end) |
| **PostgreSQL** | Banco de dados relacional |
| **Docker & Docker Compose** | Conteinerização da aplicação e dos serviços |
| **Cron** | Agendamento da tarefa de verificação diária |
| **CallMeBot API** | Integração para envio de mensagens via WhatsApp |

---

## 📋 Pré-requisitos

Antes de começar, garanta que você tenha as seguintes ferramentas instaladas em seu ambiente:

- [Docker](https://www.docker.com/get-started/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## 🚀 Como Rodar o Projeto

**1. Clone o Repositório**
```bash
git clone https://github.com/DanielErick-dev/project-strong-fitness.git
```

**2. Configure as Variáveis de Ambiente**
- Navegue até o diretório do projeto.
- Crie um arquivo chamado `.env` usando o `.env.example` como base.
- Preencha as variáveis de ambiente necessárias (chaves do Django, credenciais do banco de dados, etc.).

**3. Configure as Notificações do WhatsApp (Opcional)**
Para que o envio de relatórios via CallMeBot funcione, siga estes passos:
   - **Adicione o Contato:** Salve o número do CallMeBot no seu celular: `+34 644 33 66 63`.
   - **Envie a Mensagem de Ativação:** Abra o WhatsApp e envie a mensagem `Eu permito que o callmebot me envie mensagens` para o contato salvo.
   - **Configure o `.env`:** Você receberá sua API Key via WhatsApp. Adicione-a, junto com seu número de telefone, no arquivo `.env` nas variáveis `CALLMEBOT_PHONE_NUMBER` e `CALLMEBOT_API_KEY`.

**4. Suba os Containers**
No terminal, dentro da pasta do projeto, execute o comando:
```bash
docker-compose up --build
```

**5. Acesse a Aplicação**
Após a finalização do build, a aplicação estará disponível no seu navegador em `http://localhost:8000`.

## 📝 Roadmap e Próximos Passos
- [ ] Realizar o deploy da aplicação em um serviço de nuvem.
