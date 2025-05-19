# Sistema de Controle de Biblioteca

Este projeto é um sistema web de controle de biblioteca desenvolvido em Python usando o framework Flask. Ele permite:

- Cadastro de livros
- Cadastro de usuários
- Empréstimo e devolução de livros
- Listagem de livros disponíveis e emprestados

## Casos de Uso

1. **Cadastrar Livro**
   - Ator: Bibliotecário
   - Fluxo: Informar título, autor, ano → salvar

2. **Cadastrar Usuário**
   - Ator: Bibliotecário
   - Fluxo: Informar nome, e-mail → salvar

3. **Realizar Empréstimo**
   - Ator: Bibliotecário
   - Fluxo: Selecionar usuário e livro → confirmar empréstimo

4. **Realizar Devolução**
   - Ator: Bibliotecário
   - Fluxo: Selecionar empréstimo → marcar como devolvido

## Tecnologias

- Python 3
- Flask
- HTML/CSS (Bootstrap)
- Pickle para persistência dos dados

## Execução

```bash
pip install -r requirements.txt
python main.py
```

Acesse pelo navegador: http://localhost:5000
