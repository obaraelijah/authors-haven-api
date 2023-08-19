# Authors Haven API with Docker, NGINX, and Redis

<p>
  <a href="https://twitter.com/talkcoding" target="_blank">
    <img alt="Twitter: talkcoding" src="https://img.shields.io/twitter/follow/Talkcoding.svg?style=social" />
  </a>
</p>

👋 Welcome to the Authors Haven API project! This project showcases a powerful Django & Django Rest Framework API, containerized with Docker, and optimized with NGINX and Redis for improved performance.

## Features

- User authentication and registration
- Create, read, update, and delete articles
- Commenting system for articles
- User profiles with personalized information
- Token-based authentication for secure API access
- Efficient caching using Redis for improved performance

## Technologies Used

- Django
- Django Rest Framework
- Docker
- NGINX
- Redis
- Celery

## Getting Started

To run this project locally, you need to have Docker installed. Follow these steps:

### Prerequisites

- Docker: [Installation Guide](https://docs.docker.com/get-docker/)

### Installation

1. Clone this repository:

   ```bash
    https://github.com/obaraelijah/authors-haven-api.git
    ```
2. Navigate to the project directory:

    ```bash
    cd authors-haven-api
    ```
3. Build and run the Docker containers:

    ```bash
    Make build 
    ```
    or use 
    
    ```bash
    docker compose -f local.yml up --build -d --remove-orphans
    ```
4. Access the API at http://localhost:8080.

## Usage
After setting up the project locally, you can interact with the API using tools like curl, httpie, or API clients like Postman. Refer to the API documentation for available endpoints, request formats, and responses.

## License

This project is licensed under the MIT License.
## Acknowledgments

This project wouldn't have been possible without the invaluable resources and documentation provided by the following:

- [Django Documentation](https://docs.djangoproject.com/): The official documentation for the Django web framework, which guided us in building the backend of our project.
- [Django Rest Framework Documentation](https://www.django-rest-framework.org/): The comprehensive documentation for the Django Rest Framework, helping us create robust and user-friendly APIs.
- [Docker Documentation](https://docs.docker.com/): The Docker documentation was crucial in containerizing our application and making it portable and scalable.




