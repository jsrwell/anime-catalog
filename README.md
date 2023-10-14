# Animes Catalog REST API

Este é um servidor baseado em Flask que oferece uma API REST para gerenciar informações sobre animes. Siga as etapas abaixo para configurar e executar o servidor.

## Instalação Rápida

1. Clone o repositório:

    ```bash
    git clone https://github.com/jsrwell/anime-catalog
    cd seu-repositorio
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure o banco de dados:

    - Inicialize o banco de dados:

        ```bash
        flask db init
        ```

    - Crie uma migração:

        ```bash
        flask db migrate
        ```

    - Aplique as migrações:

        ```bash
        flask db upgrade
        ```

5. Inicie o servidor:

    ```bash
    flask run
    ```

Agora o servidor está em execução. Você pode acessar a API em `http://localhost:5000` para ver as rotas disponíveis.

## Uso

Você pode usar esta API para gerenciar informações sobre animes. Consulte a documentação da API para obter mais informações sobre como usar as rotas disponíveis.

## Autor

jsrwell
