# READ BOOK

- Este projeto se baseia em uma API REST que tem como função cadastrar livros lidos por usuários préviamente cadastrados.

<p align="center">
  <a href="#DEPENDÊNCIAS">DEPENDÊNCIAS</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#COMO USAR O PROJETO?">COMO USAR O PROJETO?</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#ROTAS">ROTAS</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#COMO CONTRIBUIR?">COMO CONTRIBUIR?</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#memo-licença">LICENÇA</a>
</p>

## DEPENDÊNCIAS
    ![Python Badge](https://www.python.org/)
    ![Flask Badge](https://flask.palletsprojects.com/en/1.1.x/)
    ![Flask-Restplus Badge](https://flask-restplus.readthedocs.io/en/stable/)
    ![Werkzeug Badge](https://werkzeug.palletsprojects.com/en/1.0.x/)
    ![SQlite Badge](https://sqlite.org/index.html)


 
## COMO USAR O PROJETO?

- CLONE O PROJETO:
    `git clone https://github.com/hiago-buzz/read-book.git`

- CRIE UM AMBIENTE VIRTUAL NA RAIZ DO PROJETO:
    * WINDOW: `virtualenv venv .env`
    * UNIX: `python3 -m venv .env`

- INICIE A VIRTUALENV:
    * WINDOW: `source .env\Script\activate`
    * UNIX: `source .env\bin\activate`

- INSTALE AS DEPENDÊNCIAS:
    `pip install -r requirements.txt`

- INICIE O SERVIDOR: `python run.py`
    Após isso o servidor iniciar em: `http://localhost:5500`

## ROTAS

- A documentação é gerada automaticamente durante o desenvolvimento com o `swagger` sendo possível visualizar em `http://localhost:5500`.
- Todas as rodas da api utilizam o prefixo `/api`, seguido do endpoint desejado, sendo necessário o parametro `user_name` nos headers de cada requisição;

EX: `http://localhost:5500/api/book`

Livros:
- `/api/book/` recebe os verbos `GET` e `POST` 

* Exemplo de payload POST:

    '''
        {
        "title": "string",
        "author": "string",
        "finish": "string",
        "genre": "string",
        "user_name": "string"
        }
    ''' 
- `/api/book/:id` recebe os métedos `GET`, `PUT` e `DELETE`

- USUÁRIOS:
...

## COMO CONTRIBUIR?

- Faça um fork desse repositório;
- Cria uma branch com a sua feature: `git checkout -b feature`;
- Faça commit das suas alterações: `git commit -m 'Minha feature'`;
- Faça push para a sua branch: `git push origin feature`.

Depois que o merge da sua pull request for feito, você pode deletar a sua branch.

## :memo: LICENÇA

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.