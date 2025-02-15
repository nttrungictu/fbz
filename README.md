# Flask Application

This is a Flask application that provides a multi-language interface and integrates with Telegram for notifications.

## Requirements

- Python 3.10
- Flask 3.0.0
- Gunicorn 21.2.0
- Werkzeug 3.1.3
- MarkupSafe 3.0.2
- Certifi 2023.7.22
- Charset Normalizer 3.2.0
- Click 8.1.3
- Idna 3.4
- Colorama 0.4.6
- Jinja2 3.1.2
- Pip 23.2.1
- Urllib3 2.0.4
- Requests 2.31.0
- Itsdangerous 2.1.2

## Setup

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd flask
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv myenv
    source myenv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    python app.py
    ```

## Docker

To run the application using Docker:

1. Build the Docker image:
    ```sh
    docker build -t flask-app .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 5000:5000 flask-app
    ```

## License

This project is licensed under the MIT License.
