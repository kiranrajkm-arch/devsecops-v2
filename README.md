# DevSecOps Security Pipeline

A hands-on DevSecOps project demonstrating how automated testing and security controls can be integrated throughout the software development lifecycle.

The project uses a Python Flask API as the sample application. It will progressively incorporate containerization, CI/CD automation, static analysis, dependency scanning, secret detection, container scanning and infrastructure-as-code security checks.

## Project Objectives

* Build a maintainable Python web application.
* Apply automated tests before accepting code changes.
* Package the application using Docker.
* Build a CI/CD pipeline with GitHub Actions.
* Detect security issues early in the development lifecycle.
* Enforce security quality gates before packaging or releasing the application.
* Document security findings and remediation decisions.

## Current Implementation

* Python Flask API
* Application information endpoint
* Health-check endpoint
* Automated unit and API tests using pytest
* Isolated Python virtual environment
* Git-based source control

## API Endpoints

| Method | Endpoint  | Description                                |
| ------ | --------- | ------------------------------------------ |
| GET    | `/`       | Returns application information and status |
| GET    | `/health` | Returns the application health status      |

## Project Structure

```text
devsecops-v2/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_app.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Run the Application Locally

### Prerequisites

* Python 3
* Git

### Setup

Create and activate a Python virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

Start the application:

```powershell
python -m app.main
```

The application will be available at:

```text
http://127.0.0.1:5000
```

## Run the Tests

```powershell
python -m pytest -v
```

The current test suite validates:

* Successful access to the main endpoint
* Expected application-status response
* Successful health-check response

## Planned DevSecOps Controls

| Stage          | Control                             | Tool           |
| -------------- | ----------------------------------- | -------------- |
| Source         | Secret detection                    | Gitleaks       |
| Build          | Static application security testing | Semgrep        |
| Dependencies   | Software composition analysis       | Trivy          |
| Test           | Automated application testing       | pytest         |
| Container      | Image vulnerability scanning        | Trivy          |
| Infrastructure | Infrastructure-as-code scanning     | Checkov        |
| CI/CD          | Automated security gates            | GitHub Actions |

## Planned Workflow

1. A developer pushes code or opens a pull request.
2. GitHub Actions starts the CI pipeline.
3. Automated tests validate application behaviour.
4. Security tools scan the source code and dependencies.
5. The pipeline builds the Docker image.
6. Trivy scans the image for known vulnerabilities.
7. Security gates prevent vulnerable builds from progressing.
8. Scan results are retained as pipeline artifacts for review.


## Author
Kiran
