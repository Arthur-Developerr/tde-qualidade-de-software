# API Flask - Gerenciamento de Usuários e Cotação USD-BRL

Uma API REST desenvolvida em Flask com funcionalidades de gerenciamento de usuários e consulta de cotação do dólar.

## ⚡ Início Rápido

```bash
# 1. Instale as dependências
pip install -r requirements.txt

# 2. Execute a aplicação
flask --app app.app run

# 3. Teste os endpoints
# Usuários
curl http://localhost:5000/api/users

# Cotação USD-BRL
curl http://localhost:5000/api/exchange/usd-to-brl
```

## 📋 Status do Projeto

- ✅ **Estrutura inicial**: Configuração do Flask e SQLAlchemy
- ✅ **Modelo de dados**: Entidade User com campos id, name e email
- ✅ **Endpoints CRUD**: Implementação completa dos endpoints de usuários
- ✅ **Banco de dados**: SQLite configurado e funcional
- ✅ **Cotação USD-BRL**: Integração com AwesomeAPI para cotação em tempo real

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

#### 👤 Gerenciamento de Usuários

| Método | Endpoint | Descrição | Status |
|--------|----------|-----------|--------|
| `GET` | `/api` | Mensagem de boas-vindas | ✅ |
| `GET` | `/api/users` | Lista todos os usuários | ✅ |
| `POST` | `/api/users` | Cria um novo usuário | ✅ |
| `PUT` | `/api/users/{id}` | Atualiza um usuário existente | ✅ |
| `DELETE` | `/api/users/{id}` | Remove um usuário | ✅ |

#### 💱 Cotação de Moedas

| Método | Endpoint | Descrição | Status |
|--------|----------|-----------|--------|
| `GET` | `/api/exchange/usd-to-brl` | Obtém cotação atual USD-BRL | ✅ |

### Exemplos de Uso

#### 👤 Usuários

**1. Listar todos os usuários**
```bash
curl -X GET http://localhost:5000/api/users
```

**2. Criar um novo usuário**
```bash
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "João Silva", "email": "joao@email.com"}'
```

**3. Atualizar um usuário**
```bash
curl -X PUT http://localhost:5000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "João Santos", "email": "joao.santos@email.com"}'
```

**4. Deletar um usuário**
```bash
curl -X DELETE http://localhost:5000/api/users/1
```

#### 💱 Cotação USD-BRL

**Obter cotação atual do Dólar**
```bash
curl http://localhost:5000/api/exchange/usd-to-brl
```

**Resposta:**
```json
{
  "code": "USD",
  "codein": "BRL",
  "name": "Dólar Americano/Real Brasileiro",
  "high": "5.4251",
  "low": "5.37139",
  "varBid": "-0.0035",
  "pctChange": "-0.064791",
  "bid": "5.3986",
  "ask": "5.4016",
  "timestamp": "1763990550",
  "create_date": "2025-11-24 10:22:30"
}
```

**API externa utilizada:** [https://economia.awesomeapi.com.br/json/last/USD-BRL](https://economia.awesomeapi.com.br/json/last/USD-BRL)

## 🗂️ Estrutura do Projeto

```
tde-qualidade-de-software/
├── app/
│   ├── __init__.py
│   ├── app.py              # Configuração principal da aplicação
│   ├── models.py           # Modelos de dados (User)
│   ├── routes.py           # Definição das rotas/endpoints
│   └── service.py          # Lógica de negócio (Users + USD-BRL)
├── tests/                  # ✨ NOVO: Testes unitários
│   ├── __init__.py
│   ├── test_exchange.py            # Testes com unittest
│   ├── test_exchange_pytest.py     # Testes com pytest
│   └── README.md                   # Documentação dos testes
├── instance/
│   └── database.sqlite     # Banco de dados SQLite
├── requirements.txt        # Dependências do projeto
└── README.md              # Este arquivo
```

## 🛠️ Tecnologias Utilizadas

- **Flask**: Framework web Python
- **SQLAlchemy**: ORM para banco de dados
- **SQLite**: Banco de dados local
- **Requests**: Biblioteca para requisições HTTP
- **AwesomeAPI**: API externa para cotações de moedas
- **Pytest**: Framework de testes
- **Python**: Linguagem de programação

## 📦 Dependências

- `flask`: Framework web
- `Flask-SQLAlchemy`: Extensão do Flask para SQLAlchemy
- `requests`: Biblioteca para requisições HTTP
- `pytest`: Framework de testes
- `pytest-cov`: Cobertura de testes

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

### Testes Unitários (com Mocks)

Os testes unitários estão na pasta `/tests` e **não fazem chamadas reais** à API externa.

```bash
# Executar todos os testes (pytest)
pytest tests/ -v

# Executar com cobertura
pytest tests/ --cov=app

# Executar testes unittest
python -m unittest tests/test_exchange.py -v
```

**✅ Todos os testes usam `unittest.mock.patch` para simular a API externa**

### Teste Manual

Para testar o endpoint manualmente com a API real:

```bash
# Iniciar a aplicação
flask --app app.app run

# Em outro terminal, testar o endpoint
curl http://localhost:5000/api/exchange/usd-to-brl
```

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Equipe

- **Arthur Sousa Furtado**
- **Pedro Manoel Gaspar Aguiar**
- **Carlos Antonio dos Santos Junior**
- **Alisson Daniel Costa Nunes**

## 👥 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'feat: adiciona AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📞 Suporte

Para dúvidas ou suporte, entre em contato através dos issues do repositório.
