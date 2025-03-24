Flask + MySQL Docker Compose Project

📜 Project Overview

This project demonstrates how to build and deploy a simple Flask application with MySQL using Docker Compose. The Flask application performs basic read and write operations on a MySQL database. The project uses Poetry for Python dependency management.

📂 Project Structure

flask_docker_compose/
│
├── app.py
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── poetry.lock
└── README.md

🚀 Features

Add a new user via URL route

Fetch all users from the database

Containerized with Docker Compose

Poetry for dependency management

⚙️ Prerequisites

Docker and Docker Compose installed

Python 3.11+

Poetry installed (pip install poetry)

🛠 Setup Instructions

1. Clone the repository

git clone git@github.com:shubhamkansal1993/docker_compose_demo.git
cd docker_compose_demo

2. Build and run with Docker Compose

docker-compose up --build

This will start both the MySQL database and the Flask web application.

3. Flask Application will be accessible at:

http://localhost:5000

📝 API Endpoints

Route                       Method   Description

/                           GET    Test route to confirm the app is running

/add_user/<username>        GET    Adds a user with the given username

/users                      GET    Retrieves all users from the database

Example Usage:

Add user:

http://localhost:5000/add_user/John

Fetch all users:

http://localhost:5000/users

📦 Dockerfile Example

FROM python:3.11-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY ./app.py ./

CMD ["poetry", "run", "python", "app.py"]

📃 docker-compose.yml Example

version: '3.8'

services:
  mysql:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: rootpass
      MYSQL_DATABASE: flaskdb
      MYSQL_USER: flaskuser
      MYSQL_PASSWORD: flaskpass
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql

  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - mysql
    environment:
      DATABASE_URL: "mysql+pymysql://flaskuser:flaskpass@mysql:3306/flaskdb"

volumes:
  mysql_data:

💻 Local Development without Docker (Optional)

Install Poetry: pip install poetry

Install dependencies: poetry install

Set environment variable:

export DATABASE_URL="mysql+pymysql://flaskuser:flaskpass@localhost:3306/flaskdb"

Run Flask app:

poetry run python app.py

📚 Additional Notes

Ensure that the MySQL container has fully started before sending requests.

The app auto-creates tables using db.create_all() on startup.

Update pyproject.toml if additional dependencies are needed.

🙋‍♂️ Questions / Issues

For any issues or questions, please raise a GitHub issue or contact Shubham Kansal.

⭐ Star this repo if it helped you!