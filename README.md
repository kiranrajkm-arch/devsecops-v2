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
