# Selenium Tests on SauceDemo

This repository contains automated tests for [SauceDemo](https://www.saucedemo.com/) using **Selenium** and **Pytest**. It is designed to improve testing skills with Selenium while ensuring reliable testing for the SauceDemo platform.

You can view the [Test Execution Plan](TestExecutionPlan.md), which serves as the foundation for the automated test suite.

## Requirements

Before running the tests, ensure that **Python** is installed on your machine. You can download it from the official Python website:

- [Download Python](https://www.python.org/downloads/)

## Installation

Follow the steps below to set up the project and install dependencies:

### 1. Clone the repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/Cicero-Henrique/selenium-tests-saucedemo.git
cd selenium-tests-saucedemo
```

### 2. Set up a virtual environment

It's recommended to create a virtual environment to isolate the project dependencies:

```bash
python -m virtualenv venv
```

### 3. Activate the virtual environment

```bash
source venv/bin/activate
```

### 4. Install project dependencies

Once the virtual environment is activated, install the required dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Running the Tests

To execute the test suite, run the following command in the terminal:

```bash
pytest
```

This will run all tests and display the results in the terminal.

### Additional Pytest Options

You can run tests with different configurations or view detailed outputs using Pytest options:

- Run tests with detailed output:

```bash
pytest -v
```

- Generate a test report:

```bash
pytest --html=report.html
```

## Project Structure

The project follows a simple structure for organizing the tests:

```bash
├── pages/                  # Page Object Models (POM) for each page
├── tests/                  # Test cases
├── conftest.py             # Pytest configuration and setup
├── requirements.txt        # Dependencies
├── TestExecutionPlan.md    # Test execution plan documentation
└── README.md               # Project documentation (this file)
```

## Browser Compatibility

The tests are configured to run on Chrome by default, but they can be easily modified to run on other browsers like Firefox. Ensure that the appropriate WebDriver is installed and accessible.

### Chrome WebDriver

Make sure the Chrome WebDriver is installed and matches your Chrome version. Place it in your system's PATH.

## License

This project is licensed under the MIT License.

Happy Testing!
