# Sistema de Objetos Perdidos do IFRNCM

## Sobre o que é o site?

O sistema é utilizado para organizar o registro e a consulta de objetos perdidos e encontrados no IFRN Campus Ceará-Mirim. O acesso ao site poderá ser feito por qualquer pessoa para consultar os objetos cadastrados.

A frequência de uso será principalmente durante a procura por objetos perdidos, permitindo consultas rápidas por informações como categoria, características, data e local. Também será utilizado pelos responsáveis pelo sistema para cadastrar, atualizar e organizar continuamente os registros dos objetos.

O sistema substituirá o atual processo informal de divulgação de objetos perdidos e encontrados, que ocorre principalmente por meio de grupos de mensagens e comunicação entre alunos e servidores.

## Pré-requisitos

* Python 3.12 ou superior;
* Git (opcional, caso o projeto seja obtido de um repositório);
* MySQL, para armazenamento dos dados do sistema;
* Chromium, instalado pelo Playwright para a execução dos testes de interface.

## Instalação

### 1. Obtenha o projeto

Clone o repositório ou copie os arquivos para a máquina e entre na pasta do projeto:

```bash
git clone <URL_DO_REPOSITORIO>
cd Sistema-Objetos-Perdidos-IFRNCM
```

### 2. Crie e ative um ambiente virtual

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

Com o ambiente virtual ativado, execute:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
```

### 4. Configure o banco de dados

O sistema utiliza um banco de dados MySQL para armazenar as informações dos administradores/responsáveis e dos objetos cadastrados.

Crie o banco de dados:

```sql
CREATE DATABASE sistema_objetos_perdidos
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Depois, execute as migrações:

```bash
flask --app run:app db upgrade
python -m flask run --debug 
```

### 5. Configure as variáveis de ambiente

Crie o arquivo `.env` na raiz do projeto e configure as informações do banco de dados:

```env
DB_USERNAME=root
DB_PASSWORD=sua_senha_do_mysql
DB_HOST=localhost
DB_PORT=3306
DB_NAME=sistema_objetos_perdidos
SECRET_KEY=uma-chave-secreta-forte
```

O arquivo `.env` não deve ser versionado, pois pode conter credenciais e chaves secretas.

No Windows (PowerShell), caso as variáveis sejam configuradas diretamente no terminal:

```powershell
$env:DB_USERNAME = "root"
$env:DB_PASSWORD = "sua_senha_do_mysql"
$env:DB_HOST = "localhost"
$env:DB_PORT = "3306"
$env:DB_NAME = "sistema_objetos_perdidos"
$env:SECRET_KEY = "uma-chave-secreta-forte"
```

Nunca compartilhe a `SECRET_KEY` nem versione o arquivo `.env` com valores reais.

## Execução

Com o ambiente virtual ativado e as variáveis configuradas:

```bash
python run.py
```

Abra http://127.0.0.1:5000 no navegador. Para encerrar o servidor, pressione `Ctrl+C`.

## Testes

Inicie a aplicação em um terminal e, em outro terminal com o ambiente virtual ativado, execute:

```bash
python -m unittest discover -s tests
```

Os testes utilizam um navegador Chromium em modo headless (`headless=True`) por meio do Playwright.

## Estrutura principal

```text
app/
├── forms/       # Formulários Flask-WTF
├── models/      # Modelos do banco de dados
├── services/    # Regras de negócio
├── static/      # CSS, JavaScript e imagens
├── templates/   # Templates Jinja2
└── routes.py    # Rotas da aplicação
config.py        # Configuração do Flask e do banco
run.py           # Ponto de entrada
requirements.txt # Dependências Python
tests/           # Testes automatizados
```
