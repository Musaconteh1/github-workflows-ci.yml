# E-Commerce Platform CI/CD

This repository contains an example CI/CD setup for an e-commerce platform using GitHub Actions.

## Setup

1. Install Python 3.x.
2. Clone this repository.
3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the tests locally:

    ```bash
    python -m unittest discover
    ```

## CI/CD Pipeline

The CI/CD pipeline is configured to run tests and generate reports on every push to the `main` branch and on every pull request targeting the `main` branch.

Check the [`.github/workflows/ci.yml`](.github/workflows/ci.yml) file for the workflow configuration.
