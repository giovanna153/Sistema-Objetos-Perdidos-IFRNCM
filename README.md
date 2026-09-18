## 🚀 Como executar o projeto

### 1. Clonar o repositório

Primeiro, clone o repositório do projeto:

```bash
git clone URL_DO_REPOSITORIO
```

Depois, entre na pasta do projeto:

```bash
cd sistema-objetos-perdidos
```

### 2. Criar o ambiente virtual

No terminal, execute:

```bash
python -m venv venv
```

Esse comando cria um ambiente virtual chamado `venv` para instalar as dependências do projeto de forma isolada.

### 3. Ativar o ambiente virtual

No **Windows**, execute:

```bash
venv\Scripts\activate
```

Se o ambiente for ativado corretamente, aparecerá algo parecido com:

```text
(venv) C:\...\sistema-objetos-perdidos>
```

### 4. Instalar as dependências

Com o ambiente virtual ativado, instale as dependências presentes no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Executar o projeto

Depois de instalar todas as dependências, execute o projeto Flask:

```bash
flask run
```

O terminal exibirá o endereço do servidor. Acesse no navegador:

```text
http://127.0.0.1:5000
```

### ⚠️ Observação

Sempre que for trabalhar no projeto, primeiro ative o ambiente virtual:

```bash
venv\Scripts\activate
```

Depois, execute o projeto:

```bash
flask run
```

Para sair do ambiente virtual, utilize:

```bash
deactivate
```
