Este `README.md` mais detalhado fornece uma visão geral abrangente do projeto, incluindo a estrutura de pastas, descrição dos arquivos, como executar o projeto e como usar suas funcionalidades.


# Aplicação CRUD

Esta é uma aplicação simples de CRUD (Criar, Ler, Atualizar, Deletar) usando Python, Tkinter para a interface gráfica e JSON para armazenamento de dados.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
Crud/
├── data/
│ └── persons.json # Arquivo JSON onde os dados das pessoas são armazenados
├── src/
│ ├── crud_logic.py # Módulo com a lógica de CRUD
│ ├── gui.py # Módulo com a interface gráfica
│ ├── person.py # Módulo com a classe Person
├── README.md # Arquivo de documentação do projeto
└── main.py # Arquivo principal para iniciar a aplicação
```


### `data/persons.json`
Arquivo JSON que armazena os dados das pessoas. Se não existir, será criado automaticamente ao iniciar a aplicação.

### `src/crud_logic.py`
Módulo que contém a lógica de CRUD para gerenciar pessoas. Funções principais:
- `get_persons()`: Retorna a lista de pessoas.
- `add_person(name, phone, email)`: Adiciona uma nova pessoa.
- `update_person(name, phone, email)`: Atualiza uma pessoa existente.
- `delete_person(person_id)`: Deleta uma pessoa.
- `search_person(query)`: Busca pessoas pelo nome.
- `create_empty_json()`: Cria um arquivo JSON vazio se não existir.

### `src/gui.py`
Módulo que contém a interface gráfica da aplicação usando Tkinter. Funções principais:
- `CRUDApplication`: Classe principal da aplicação com métodos para adicionar, atualizar, deletar e buscar pessoas.
- `fill_entry_fields(event)`: Preenche os campos de entrada ao selecionar uma pessoa na lista.
- `update_person_listbox()`: Atualiza a lista de pessoas exibida na interface gráfica.
- `clear_entries()`: Limpa os campos de entrada.

### `src/person.py`
Módulo que contém a classe `Person`. Funções principais:
- `to_dict()`: Converte um objeto Person para um dicionário.
- `from_dict(data)`: Cria um objeto Person a partir de um dicionário.
- `load_from_json(filename)`: Carrega a lista de pessoas a partir de um arquivo JSON.

## Funcionalidades

- **Adicionar Pessoa**: Adicione uma nova pessoa com nome, telefone e email.
- **Buscar Pessoa**: Busque pessoas pelo nome.
- **Atualizar Pessoa**: Atualize os detalhes de uma pessoa existente.
- **Deletar Pessoa**: Delete uma pessoa.
- **Exibir Lista de Pessoas**: Veja a lista de todas as pessoas cadastradas.
- **Criação Automática de Arquivo JSON**: Se o arquivo `persons.json` não existir, ele será criado automaticamente com uma lista vazia.

## Exemplo de Uso

### Adicionar uma Pessoa

- Preencha os campos "Nome", "Telefone" e "Email".
- Clique no botão "Adicionar".

### Buscar uma Pessoa

- Digite o nome da pessoa no campo "Nome".
- Clique no botão "Buscar".

### Atualizar uma Pessoa

- Selecione uma pessoa da lista exibida.
- Os campos serão preenchidos com os dados da pessoa selecionada.
- Modifique os campos conforme necessário.
- Clique no botão "Atualizar".

### Deletar uma Pessoa

- Selecione uma pessoa da lista exibida.
- Clique no botão "Deletar".
- Confirme a exclusão na janela de diálogo que aparecer.

### Exibir Lista de Pessoas

- Todas as pessoas cadastradas são exibidas na lista.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias e correções.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.
