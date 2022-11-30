# Requisitos para utilizar a aplicação e guia

1. Crie um ambiente virtual para o projeto (python -m venv venv).
2. Acesse seu ambiente virtual(source venv/bin/activate) - Linux, para ambiente windows (<venv>\Scripts\Activate.ps1). Em caso de duvidas consulte a doc https://docs.python.org/pt-br/dev/library/venv.html
3. Instalar dependencias do projeto (pip install -r requirements.txt.
4. Rodar as migração (./manage.py migrate ou python manage.py migrate)
5. Por fim, rodar o servidor(./manage.py runserver ou python manage.py runserver)


# Como testar

1. Acessar seu localhost na porta 8000 pelo seu cliente web usando o endpoint '/user/upload/' (http://127.0.0.1:8000/user/upload/)
2. Click em 'escolher arquivo' e escolha o arquivo CNAB.txt que está na raiz do projeto e por fim click em 'upload'
3. Vá até o seu db.sqlite3, entre na tabela 'users.user' e confira o resultado.