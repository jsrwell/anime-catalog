# Animes Catalog REST API

This is a Flask-based server that provides a REST API for managing anime information. Follow the steps below to set up and run the server.

## Quick Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/jsrwell/anime-catalog
    cd your-repository
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure the database:

    - Initialize the database:

        ```bash
        flask db init
        ```

    - Create a migration:

        ```bash
        flask db migrate
        ```

    - Apply the migrations:

        ```bash
        flask db upgrade
        ```

5. Start the server:

    ```bash
    flask run
    ```

Now the server is up and running. You can access the API at `http://localhost:5000` to view the available routes.

## Usage

You can use this API to manage anime information. Refer to the API documentation for more details on how to use the available routes.

## Author

jsrwell
