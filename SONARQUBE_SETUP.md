# 🔍 Configuração do SonarQube

Este guia explica como configurar e executar a análise do SonarQube no projeto.

## 📋 Pré-requisitos

1. Pytest e pytest-cov instalados:
```bash
pip install -r requirements.txt
```

2. SonarQube Scanner instalado (ou usar via Docker)

---

## 🚀 Passo 1: Gerar Relatório de Cobertura

Execute os testes com geração do relatório de cobertura:

```bash
pytest --cov=app --cov-report=xml:coverage.xml tests/
```

**O que esse comando faz:**
- `--cov=app` → Mede a cobertura do código na pasta `app/`
- `--cov-report=xml:coverage.xml` → Gera o arquivo `coverage.xml`
- `tests/` → Executa os testes da pasta `tests/`

### Comandos Adicionais Úteis:

```bash
# Ver relatório de cobertura no terminal
pytest --cov=app --cov-report=term-missing tests/

# Gerar relatório HTML (para visualizar no navegador)
pytest --cov=app --cov-report=html tests/
# Depois abra: htmlcov/index.html

# Gerar XML + ver no terminal
pytest --cov=app --cov-report=xml:coverage.xml --cov-report=term-missing tests/
```

---

## 📄 Passo 2: Verificar Arquivo de Configuração

O arquivo `sonar-project.properties` já está configurado com:

```properties
sonar.projectKey=tde-qualidade-software
sonar.sources=app
sonar.tests=tests
sonar.python.coverage.reportPaths=coverage.xml
```

### Personalizações Importantes:

Se você estiver usando SonarCloud ou um servidor SonarQube específico, pode precisar adicionar:

```properties
# Para SonarCloud
sonar.organization=sua-organizacao
sonar.host.url=https://sonarcloud.io

# Para SonarQube local
sonar.host.url=http://localhost:9000
```

---

## 🔧 Passo 3: Executar Análise do SonarQube

### Opção A: Usando SonarQube Scanner (CLI)

```bash
sonar-scanner
```

### Opção B: Usando Docker

```bash
docker run --rm -e SONAR_HOST_URL="http://seu-sonar:9000" \
  -e SONAR_LOGIN="seu-token" \
  -v "$(pwd):/usr/src" \
  sonarsource/sonar-scanner-cli
```

### Opção C: Via GitHub Actions / CI/CD

Adicione ao seu workflow:

```yaml
- name: Generate coverage report
  run: pytest --cov=app --cov-report=xml:coverage.xml tests/

- name: SonarCloud Scan
  uses: SonarSource/sonarcloud-github-action@master
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```

---

## ✅ Verificação

Após gerar o relatório, você deve ver o arquivo `coverage.xml` na raiz do projeto:

```bash
# Windows
dir coverage.xml

# Linux/Mac
ls -l coverage.xml
```

O arquivo deve conter XML com informações de cobertura:

```xml
<?xml version="1.0" ?>
<coverage version="7.x.x" timestamp="..." ...>
  <packages>
    <package name="app">
      ...
    </package>
  </packages>
</coverage>
```

---

## 📊 Exemplo de Execução Completa

```bash
# 1. Executar testes com cobertura
pytest --cov=app --cov-report=xml:coverage.xml --cov-report=term tests/

# Resultado esperado:
# tests/test_exchange_pytest.py::TestExchangeService::test_get_usd_brl_rate_success PASSED
# tests/test_exchange_pytest.py::TestExchangeService::test_get_usd_brl_rate_api_error PASSED
# ...
# ---------- coverage: platform win32, python 3.x.x -----------
# Name                    Stmts   Miss  Cover
# -------------------------------------------
# app\__init__.py             0      0   100%
# app\service.py             25      2    92%
# app\routes.py              15      1    93%
# -------------------------------------------
# TOTAL                      40      3    92%

# 2. Verificar arquivo gerado
dir coverage.xml

# 3. Executar SonarQube (se configurado)
sonar-scanner
```

---

## 🎯 Métricas que o SonarQube Vai Analisar

Com o `coverage.xml`, o SonarQube mostrará:

- ✅ **Cobertura de Código** → Porcentagem de código testado
- ✅ **Linhas Cobertas** → Quais linhas foram executadas nos testes
- ✅ **Linhas Não Cobertas** → Quais linhas não têm testes
- ✅ **Complexidade** → Análise de complexidade do código
- ✅ **Code Smells** → Possíveis problemas no código
- ✅ **Bugs Potenciais** → Padrões que podem causar bugs
- ✅ **Vulnerabilidades** → Problemas de segurança

---

## 📁 Estrutura Esperada

```
tde-qualidade-de-software/
├── app/                           # Código fonte (analisado)
├── tests/                         # Testes (analisados separadamente)
├── sonar-project.properties       # ✨ Configuração do SonarQube
├── coverage.xml                   # ✨ Relatório de cobertura
├── .gitignore                     # (coverage.xml não vai pro Git)
└── requirements.txt
```

---

## 🔍 Troubleshooting

### Erro: "No coverage data collected"

**Problema:** Testes não geraram cobertura.

**Solução:**
```bash
# Certifique-se de especificar o diretório correto
pytest --cov=app tests/
```

---

### Erro: "sonar-scanner not found"

**Problema:** SonarQube Scanner não está instalado.

**Solução:**
- Instale: https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/
- Ou use Docker (veja Opção B acima)

---

### SonarQube não encontra coverage.xml

**Problema:** Caminho do arquivo incorreto.

**Solução:** Verifique se o arquivo está na raiz:
```bash
# O arquivo deve estar aqui:
./coverage.xml

# E o sonar-project.properties deve ter:
sonar.python.coverage.reportPaths=coverage.xml
```

---

## 📝 Resumo dos Comandos

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Executar testes com cobertura
pytest --cov=app --cov-report=xml:coverage.xml tests/

# 3. (Opcional) Ver cobertura no terminal
pytest --cov=app --cov-report=term-missing tests/

# 4. Executar análise do SonarQube
sonar-scanner
```

---

## ✅ Checklist

Antes de executar o SonarQube, verifique:

- [ ] Testes estão passando
- [ ] `coverage.xml` foi gerado
- [ ] `sonar-project.properties` está configurado
- [ ] SonarQube Scanner está instalado/configurado
- [ ] Token de autenticação está configurado (se necessário)

---

## 🎓 Para Apresentação no TDE

Mostre:

1. **Execução dos testes:**
   ```bash
   pytest tests/ -v
   ```

2. **Geração da cobertura:**
   ```bash
   pytest --cov=app --cov-report=term-missing tests/
   ```

3. **Arquivo XML gerado:**
   ```bash
   type coverage.xml  # Windows
   cat coverage.xml   # Linux/Mac
   ```

4. **Configuração do Sonar:**
   - Mostre o arquivo `sonar-project.properties`
   - Explique cada linha

5. **(Se possível) Resultado no SonarQube:**
   - Screenshot do dashboard
   - Métricas de cobertura
   - Code quality

---

**🎉 Pronto para análise do SonarQube!**

