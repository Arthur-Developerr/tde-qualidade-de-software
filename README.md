# API Flask - Gerenciamento de Usuários

Uma API REST simples desenvolvida em Flask para gerenciamento de usuários com operações CRUD completas.

## 📋 Status do Projeto

- ✅ **Estrutura inicial**: Configuração do Flask e SQLAlchemy
- ✅ **Modelo de dados**: Entidade User com campos id, name e email
- ✅ **Endpoints CRUD**: Implementação completa dos endpoints
- ✅ **Banco de dados**: SQLite configurado e funcional
- 🔄 **Em desenvolvimento**: Testes automatizados e documentação da API

## 🚀 Instruções de Execução

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação e Execução

1. **Clone o repositório**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd tde-qualidade-de-software
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **Linux/Mac:**
   ```bash
   source venv/bin/activate
   ```

4. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

5. **Execute a aplicação**
   ```bash
   python app/app.py
   ```

6. **Acesse a API**
   - A aplicação estará rodando em `http://localhost:5000`
   - Endpoint de boas-vindas: `http://localhost:5000/api`

## 📡 Endpoints da API

### Base URL
```
http://localhost:5000/api
```

### Endpoints Disponíveis

| Método | Endpoint | Descrição | Status |
|--------|----------|-----------|--------|
| `GET` | `/api` | Mensagem de boas-vindas | ✅ |
| `GET` | `/api/users` | Lista todos os usuários | ✅ |
| `POST` | `/api/users` | Cria um novo usuário | ✅ |
| `PUT` | `/api/users/{id}` | Atualiza um usuário existente | ✅ |
| `DELETE` | `/api/users/{id}` | Remove um usuário | ✅ |

### Exemplos de Uso

#### 1. Listar todos os usuários
```bash
curl -X GET http://localhost:5000/api/users
```

#### 2. Criar um novo usuário
```bash
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "João Silva", "email": "joao@email.com"}'
```

#### 3. Atualizar um usuário
```bash
curl -X PUT http://localhost:5000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "João Santos", "email": "joao.santos@email.com"}'
```

#### 4. Deletar um usuário
```bash
curl -X DELETE http://localhost:5000/api/users/1
```

## 🗂️ Estrutura do Projeto

```
tde-qualidade-de-software/
├── app/
│   ├── __init__.py
│   ├── app.py              # Configuração principal da aplicação
│   ├── models.py           # Modelos de dados (User)
│   ├── routes.py           # Definição das rotas/endpoints
│   └── service.py          # Lógica de negócio
├── instance/
│   └── database.sqlite     # Banco de dados SQLite
├── requirements.txt        # Dependências do projeto
└── README.md              # Este arquivo
```

## 🛠️ Tecnologias Utilizadas

- **Flask**: Framework web Python
- **SQLAlchemy**: ORM para banco de dados
- **SQLite**: Banco de dados local
- **Python**: Linguagem de programação

## 📦 Dependências

- `flask`: Framework web
- `Flask-SQLAlchemy`: Extensão do Flask para SQLAlchemy

## 🔧 Comandos Git - Fluxo de Trabalho

### Criação do repositório local e primeiro push

```bash
# Criar diretório e inicializar repositório
mkdir tde-qualidade-de-software && cd tde-qualidade-de-software
git init
git branch -M main

# Criar ambiente virtual e instalar dependências
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Criar arquivos do projeto (app.py, models.py, etc.)
# Adicionar e commitar estrutura inicial
git add .
git commit -m "feat: estrutura inicial do projeto Flask"

# Criar repositório remoto no GitHub/GitLab e conectar
git remote add origin <URL_DO_REPO>
git push -u origin main
```

### Criar branches e fluxo de feature

```bash
# Criar branch develop
git checkout -b develop
git push -u origin develop

# Criar feature branch
git checkout -b feature/users-crud
# Desenvolver funcionalidades, adicionar e commitar alterações
git add app/
git commit -m "feat(users): adicionar endpoints GET/POST /users"

# Push e abrir Pull Request
git push -u origin feature/users-crud
# Após revisão, mesclar feature em develop via PR/MR
```

### Sincronizar e atualizar branches

```bash
# Atualizar develop
git checkout develop
git pull origin develop

# Rebase/merge da develop na feature (opcional)
git checkout feature/users-crud
git rebase develop
# ou
git merge develop
```

### Boas práticas de commits

- Use mensagens curtas e padronizadas:
  - `feat(...)`: Nova funcionalidade
  - `fix(...)`: Correção de bug
  - `chore(...)`: Tarefas de manutenção
  - `docs(...)`: Documentação
  - `test(...)`: Testes
  - `refactor(...)`: Refatoração de código

- Evite commits gigantes — prefira pequenos commits lógicos
- Exemplos:
  ```bash
  git commit -m "feat(users): adicionar endpoint POST /users"
  git commit -m "fix(users): corrigir validação de email"
  git commit -m "docs: atualizar README com novos endpoints"
  git commit -m "test(users): adicionar testes para CRUD de usuários"
  ```

## 🧪 Testes

*Em desenvolvimento - testes automatizados serão implementados em breve*

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'feat: adiciona AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📞 Suporte

Para dúvidas ou suporte, entre em contato através dos issues do repositório.
