# Rest-Auth-API

| MAINTAINER | Jesus Pombo | Jesus-15 | s5219967@bournemouth.ac.uk |

This module introduces comprehensive CRUD (Create, Read, Update, Delete) operations for user authentication in the RESTful API. The goal is to enhance the authentication system by allowing users to manage their accounts through standard HTTP methods.

Implementing the `/api/users` endpoint for creating new user accounts using a POST request.
Added `/api/login` endpoint for user authentication through a POST request.
Introduced `/api/users/<int:id>` endpoint to retrieve user details using a GET request.
Created a `/api/users/<int:id>` endpoint for updating user information via a PUT request.
Implemented a `/api/users/<int:id>` endpoint for deleting user accounts using a DELETE request.

# Additional Notes:

The codebase has been thoroughly tested, and all tests pass successfully.
This feature aligns with any project authentication design and enhances the overall user experience.

# Installation Locally

If you are on Windows, to use it locally please do the following:

    $ python -m venv .venv
    $ .venv/Scripts/Activate.ps1
    (venv) $ pip install -r requirements.txt

# Running Locally

To run the server use the following command:

    (venv) $ python api.py

# Installation Docker

Just need to run the following command

    $ docker-compose up -d

# Use PHPMyAdmin for Visualization

The objective of this is to use PHPMyAdmin as a Docker image into our project to facilitate database visualization and management.

This is running on port 8080:80

# Postman Collection for API Testing

We have created a Postman collection that enables developers and testers to efficiently interact with our API endpoints, streamlining the testing and development process.

If need it please send a message to s5219967@bournemouth.ac.uk and I will add you to the workspace

# Use this command to reset docker

 $ ./reset_docker.sh
