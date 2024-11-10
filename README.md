
## Badges

<p align="center">
    <img src="https://github.com/thalissonvs/fastapi-todolist/actions/workflows/tests.yaml/badge.svg" alt="Tests">
    <img src="https://tokei.rs/b1/github/thalissonvs/fastapi-todolist" alt="Total lines">
    <img src="https://tokei.rs/b1/github/thalissonvs/fastapi-todolist?category=files" alt="Files">
    <img src="https://tokei.rs/b1/github/thalissonvs/fastapi-todolist?category=comments" alt="Comments">
</p>

## About the Project

The zero_fastapi demonstrates a straightforward implementation of a REST API built with FastAPI. The 
application implements a todo list system featuring task management capabilities including task 
creation, description updates, status modifications, and comprehensive user authentication. Full API 
documentation is available at [our Redoc interface](https://zero-fastapi.fly.dev/redoc).

## Getting Started

### Cloud Testing
The API is deployed and available for testing at `https://zero-fastapi.fly.dev/`

### Local Deployment
Prerequisites:
- Docker installed on your system

To run locally, simply execute:
```bash
docker compose up
```

### Configuration

The application requires environment variables to be set in a .env file:
```plaintext
# Required Environment Variables
DATABASE_URL="YOUR_DATABASE_URL"    # Your database connection string
SECRET_KEY="your-secret-key"       # JWT secret key
ALGORITHM="HS256"                  # JWT encryption algorithm
ACCESS_TOKEN_EXPIRE_MINUTES=30     # Token expiration time in minutes
```
