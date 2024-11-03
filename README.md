# Employee Management API

This project is a RESTful API for managing employees within a company, focusing on basic CRUD operations, token-based authentication, and documentation.

- To view the documentation head on to /swagger url [LIve url](https://python.dailytrack.xyz/swagger)


## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [License](#license)

## Overview

The Employee Management API provides endpoints for creating, retrieving, updating, and deleting employee records. It is designed to showcase RESTful principles, including proper HTTP methods, response status codes, and token-based authentication.

## Features

- **CRUD Operations**: Create, read, update, and delete employee records.
- **Filtering and Pagination**: Filter employees by department and role, with pagination support.
- **Token-Based Authentication**: Secure access to all endpoints using JWT tokens.
- **Validation and Error Handling**: Comprehensive validation of employee data and appropriate error responses.
- **Swagger Documentation**: Interactive API documentation is available.

## Tech Stack

- **Backend**: Python, Flask
- **Authentication**: JWT (JSON Web Token)
- **Documentation**: Swagger UI

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Virtual environment setup

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/employee-management-api.git
   cd employee-management-api

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate

3. Install dependencies:

    ```bash
    pip install -r requirements.txt

4. Set up environment variables in a .env file:
    ```plaintext
    SECRET_KEY=your_secret_key
    DATABASE_URI=your_database_uri

5. Run the server:
    ```bash
    python app.py
